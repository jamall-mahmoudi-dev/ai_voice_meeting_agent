from stt_agent import speech_to_text
from llm_agent import summarize_meeting
from tts_agent import text_to_speech

def process_meeting(audio_file: str):
    text = speech_to_text(audio_file)
    summary = summarize_meeting(text)
    audio_summary_file = text_to_speech(summary)
    return {"transcript": text, "summary": summary, "summary_audio": audio_summary_file}
