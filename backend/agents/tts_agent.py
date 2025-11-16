import requests
from config import ELEVENLABS_API_KEY

def text_to_speech(text: str, output_file="output.mp3"):
    url = "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice": "alloy",  # انتخاب صدا
        "format": "mp3"
    }
    response = requests.post(url, json=data, headers=headers)
    with open(output_file, "wb") as f:
        f.write(response.content)
    return output_file
