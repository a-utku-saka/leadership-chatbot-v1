import whisper
import os

# install the Whisper model
model = whisper.load_model("base") 

# Folder with MP3 files
audio_folder = "downloads"

# Folder for storing output text files
output_folder = "transcriptions"
os.makedirs(output_folder, exist_ok=True)

def transcribe_audio(audio_path, output_text_path):
    """It converts the given MP3 file to text with Whisper and saves it."""
    print(f"Transcribing: {audio_path}...")
    result = model.transcribe(audio_path)
    
    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"Transcription saved: {output_text_path}")

# Tüm MP3 dosyalarını işle
for file in os.listdir(audio_folder):
    if file.endswith(".mp3"):
        audio_path = os.path.join(audio_folder, file)
        output_text_path = os.path.join(output_folder, file.replace(".mp3", ".txt"))
        transcribe_audio(audio_path, output_text_path)

print("Tüm dosyalar transkripsiyon edildi ve kaydedildi!")
