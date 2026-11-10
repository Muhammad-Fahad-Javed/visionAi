
import os

from dotenv import load_dotenv
from google import genai
from PIL import Image
from gtts import gTTS
from io import BytesIO
from google.genai import types

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "Gemini API key is missing. "
        "Please add it to your .env file."
    )


# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.6-flash"


def describe_scene(image):
    """
    Describe the surroundings visible in an image.
    """

    prompt = """
    You are Vision AI, an assistive visual assistant
    for blind and visually impaired people.

    Describe the image in simple, clear language.

    Instructions:
    1. Mention important people and objects.
    2. Describe their approximate image positions:
       left, center, or right.
    3. Mention visible doors, furniture, and obstacles.
    4. Keep the description concise.
    5. Never guess details that are not visible.
    6. Clearly mention uncertainty when necessary.
    7. Do not claim to know what is behind the camera.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image]
    )

    return response.text


def ask_question(image, question):
    """
    Answer a user's question about the camera image.
    """

    prompt = f"""
    You are Vision AI, an assistive visual assistant
    for blind and visually impaired people.

    Answer the user's question using the image.

    User question: {question}

    Rules:
    - Use simple and concise language.
    - Only describe information supported by the image.
    - Do not invent objects or people.
    - Mention uncertainty when necessary.
    - Give approximate image positions when helpful.
    - Never claim to know what is outside the image.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image]
    )

    return response.text
def ask_question_by_voice(image, audio_bytes):

    prompt = """
    You are Vision AI, an assistive visual assistant
    for blind and visually impaired people.

    Listen to the user's spoken question.
    Understand the question and answer it using the image.

    Keep your answer simple, clear and concise.
    Do not guess or invent information.
    """

    audio_part = types.Part.from_bytes(
        data=audio_bytes,
        mime_type="audio/wav"
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image, audio_part]
    )

    return response.text


def text_to_speech(text):

    speech = gTTS(text=text, lang="en")

    audio_file = BytesIO()
    speech.write_to_fp(audio_file)

    return audio_file.getvalue()