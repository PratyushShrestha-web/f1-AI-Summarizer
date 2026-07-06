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
You are an expert Formula 1 race analyst.

Summarize the following race in 3-5 sentences.

Focus only on important race events.

Race Events:

{prompt}
"""
    )

    return response.text