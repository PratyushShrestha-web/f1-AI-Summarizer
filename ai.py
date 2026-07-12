from google import genai
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Read the API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Create a Gemini client
client = genai.Client(api_key=api_key)


def generate_summary(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are an expert Formula 1 journalist.

Write a professional race report.

Requirements:
- 3–5 short paragraphs.
- Explain the flow of the race.
- Mention important incidents.
- Mention safety cars or yellow flags if present.
- Keep a professional, engaging tone.
- Do not invent facts.
Race Events:

{prompt}
"""
    )

    return response.text