
import re
from google import genai

import os
from dotenv import load_dotenv
load_dotenv()
DEBUG:bool = os.getenv("DEBUG") == "True"


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def think(user_input):
    """
    Decode the natural-language user command into a structured Python dictionary.
    """
    prompt = f"""
    Hello 
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    response = think("type hey jason")
    print("AI response:", response)