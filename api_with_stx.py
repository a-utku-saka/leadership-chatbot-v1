import requests
import os
from config import DEEPGRAM_API_KEY

# Deepgram API Key
API_KEY = DEEPGRAM_API_KEY

# Folder with MP3 files
audio_folder = "downloads"
output_folder = "transcriptions0"
os.makedirs(output_folder, exist_ok=True)

def transcribe_audio_deepgram(audio_path):
    """Translates MP3 file to Turkish text using Deepgram API."""
    print(f"Transcribing: {audio_path}...")

    url = "https://api.deepgram.com/v1/listen"
    headers = {
        "Authorization": f"Token {API_KEY}"
    }
    params = {
        "language": "tr"  # We added Turkish support!
    }

    with open(audio_path, "rb") as audio_file:
        response = requests.post(url, headers=headers, files={"audio": audio_file}, params=params)

    if response.status_code == 200:
        text = response.json()["results"]["channels"][0]["alternatives"][0]["transcript"]
        return text
    else:
        print(f"Error: {response.json()}")
        return None

# Process all MP3 files
for file in os.listdir(audio_folder):
    if file.endswith(".mp3"):
        audio_path = os.path.join(audio_folder, file)
        output_text_path = os.path.join(output_folder, file.replace(".mp3", ".txt"))

        transcript = transcribe_audio_deepgram(audio_path)
        if transcript:
            with open(output_text_path, "w", encoding="utf-8") as f:
                f.write(transcript)
            print(f"Transcription saved: {output_text_path}")
        else:
            print(f"Transcription failed for: {file}")

print(" Tüm dosyalar başarıyla Türkçeye transkribe edildi!")
