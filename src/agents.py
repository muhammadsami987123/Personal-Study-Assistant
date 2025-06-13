import google.generativeai as genai
import os

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