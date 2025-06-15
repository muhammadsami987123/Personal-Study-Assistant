import streamlit as st
import chainlit as cl
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Define the SummarizerAgent class
class SummarizerAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-001')

    def summarize_content(self, content: str, max_words: int = 200) -> str:
        prompt = f"""
        You are a helpful study assistant. Only answer educational questions (math, science, learning, etc.).
        If the question is not educational, politely decline.
        Answer in {max_words} words or less. Focus only on relevant study information.
        
        Question: {content}
        """
        response = self.model.generate_content(prompt)
        return response.text

    def stream_content(self, content: str, max_words: int = 200):
        prompt = f"""
        You are a helpful study assistant. Only answer educational questions (math, science, learning, etc.).
        If the question is not educational, politely decline.
        Answer in {max_words} words or less. Focus only on relevant study information.
        
        Question: {content}
        """
        response = self.model.generate_content(prompt, stream=True)
        for chunk in response:
            if hasattr(chunk, 'text') and chunk.text:
                yield chunk.text

# Initialize the agent
api_key = os.getenv("GEMINI_API_KEY")
summarizer = SummarizerAgent(api_key)

# Streamlit App
st.title("🎓 Personal Study Assistant")
st.write(
    """
    I'm your AI study companion! I can help you with:
    - Math problems and concepts
    - Science topics and explanations
    - Programming languages (Python, Java, JavaScript, C++, etc.)
    - Study techniques and time management
    - Learning strategies and memory techniques
    - Test preparation tips
    - Code debugging and best practices
    - Software development concepts
    """
)

user_input = st.text_input("Ask me a question:", "")

if user_input:
    st.write("Thinking...")
    
    # Summarize or stream response
    response_text = ""
    for chunk in summarizer.stream_content(user_input, max_words=200):
        response_text += chunk
        st.text(response_text)
    
    st.write(response_text)
