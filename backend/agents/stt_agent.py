import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def speech_to_text(audio_file_path: str) -> str:
    with open(audio_file_path, "rb") as audio_file:
        transcript = openai.Audio.transcriptions.create(
            file=audio_file,
            model="whisper-1"
        )
    return transcript['text']
