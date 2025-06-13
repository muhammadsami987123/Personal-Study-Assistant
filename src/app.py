import chainlit as cl
import os
from dotenv import load_dotenv
from agents import SummarizerAgent

# Load environment variables
load_dotenv()

# Initialize agent
api_key = os.getenv("GEMINI_API_KEY")
summarizer = SummarizerAgent(api_key)

@cl.on_chat_start
async def start():
    await cl.Message(
        content=(
            "# 🎓 Personal Study Assistant\n"
            "I'm your AI study companion! I can help you with:\n"
            "• Math problems and concepts\n"
            "• Science topics and explanations\n"
            "• Programming languages (Python, Java, JavaScript, C++, etc.)\n"
            "• Study techniques and time management\n"
            "• Learning strategies and memory techniques\n"
            "• Test preparation tips\n"
            "• Code debugging and best practices\n"
            "• Software development concepts\n\n"
        )
    ).send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content.strip()
    msg = cl.Message(content="")
    await msg.send()
    # Stream Gemini response chunk by chunk
    for chunk in summarizer.stream_content(user_input, max_words=200):
        msg.content += chunk
        await msg.update()
    msg.content = msg.content.strip()
    await msg.update()

# Example queries:
# - "How do I prepare for a math exam?"
# - "What is 5 + 4?"
# - "Hi, how are you?"
# - "Tell me a joke." 