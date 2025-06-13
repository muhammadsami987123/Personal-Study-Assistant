# Personal Study Assistant (Streaming Chatbot)

An AI-powered chatbot that helps students and learners with study questions, math, science, programming, and more. Powered by Gemini and Chainlit, it streams answers in real time for a modern, responsive experience.

## Features

- 🤖 Simple conversational chatbot
- 📝 Answers study, math, science, and general questions
- ⚡ Real-time streaming output (see answers as they are generated)
- 🌐 Powered by Gemini API and Chainlit

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd personal-study-assistant
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Running the Application

1. Start the Chainlit application:
```bash
chainlit run src/app.py
```

2. Open your browser and navigate to `http://localhost:8000`

## Usage

- Type any question or prompt (math, science, programming, study tips, etc.)
- The assistant will stream the answer in real time as it is generated

### Example Prompts
- How do I prepare for a math exam?
- What is 5 + 4?
- Explain Newton's laws of motion.
- Tips for learning a new language?
- Tell me a joke.

## Project Structure

- `src/agents.py`: Contains the SummarizerAgent (Gemini streaming logic)
- `src/app.py`: Main Chainlit application (chatbot logic)

## Requirements

- Python 3.9+
- Gemini API key
- Internet connection

## License

MIT License
