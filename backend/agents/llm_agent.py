import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_meeting(text: str) -> str:
    prompt = f"خلاصه نکات کلیدی جلسه زیر را به فارسی یا انگلیسی استخراج کن:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']
