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
You are V6 Turbo AI, an expert Formula 1 race intelligence assistant.

Your task is to analyze the race events provided below and produce a professional race report.

Rules:
- Only use the supplied race events.
- Never invent drivers, teams, positions, overtakes, pit stops, crashes, or penalties.
- If information is missing, simply omit it.
- Keep the report concise and professional.
- Write in the style of Formula1.com or Autosport.

Return your response using EXACTLY this format:

## Race Overview
(2-3 sentences summarizing how the race unfolded.)

## Key Incidents
(Bullet list of the most important race events.)

## Race Analysis
(Explain how the incidents affected the race.)

## Final Verdict
(Short concluding paragraph.)

Race Events:

{prompt}
"""
    )

    return response.text