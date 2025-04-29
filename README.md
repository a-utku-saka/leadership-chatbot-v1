# 🌟 Leadership Chatbot — AI-Powered Conversational Assistant

Welcome to the **Leadership Chatbot**, an AI-powered assistant that provides insightful answers to your leadership-related questions using real-world conversations and expert interviews. This project integrates cutting-edge technologies to deliver meaningful, context-based responses sourced from transcribed YouTube leadership talks.

---

## 🎯 Project Objective

The goal of this chatbot is to **analyze long-form leadership content**, store it intelligently, and allow users to ask natural language questions that receive precise and contextually grounded answers.

---

## 🧠 How It Works

This chatbot leverages a powerful pipeline:

1. 🎬 **YouTube Video Downloader**  
   - Uses `yt_dlp` to download audio from selected leadership videos.

2. 🗣 **Speech-to-Text Transcription**  
   - Converts MP3 audio to text using **OpenAI Whisper** or **Deepgram API**.

3. 📚 **Vector Embedding + FAISS Indexing**  
   - Transcripts are embedded using `sentence-transformers` and stored in a **FAISS vector database** for semantic search.

4. 🤖 **Chat Interface with GPT-4o**  
   - When a user submits a question, relevant transcript passages are retrieved from FAISS and passed to **GPT-4o** for summarization and response generation.

5. 🧩 **Web Interface (HTML/CSS/JS)**  
   - A modern, sleek UI with loading animation, dynamic response rendering, and an interactive prompt area.

---

## 🚀 Technologies Used

| Tool/Service       | Purpose                                  |
|--------------------|------------------------------------------|
| `Flask`            | Backend API                              |
| `OpenAI GPT-4o`    | Intelligent answer generation            |
| `FAISS`            | Semantic vector search                   |
| `sentence-transformers` | Embedding textual data             |
| `yt_dlp`           | YouTube audio downloader                 |
| `whisper` / `Deepgram` | Audio-to-text transcription         |
| `HTML/CSS/JavaScript` | Frontend UI for end users            |
| `Render / Fly.io`  | Hosting and deployment platforms         |



---

## 💻 Local Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/leadership-chatbot.git
   cd leadership-chatbot
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set your environment variables**  
   Create a `.env` file with:
   ```
   OPENAI_API_KEY=your-openai-key
   ```

4. **Run the Flask server**
   ```bash
   python app.py
   ```

5. Open your browser at `http://localhost:5000`

---

## 🌍 Deployment Options

- [x] **Render.com** — easy-to-use, auto-deploy via GitHub  
- [x] **Fly.io** — lightweight, fast boot, great for small-scale AI apps  
- [x] **Railway.app** — sleek UI, great GitHub integration  
- [ ] **Google Cloud Run** — serverless scaling, ideal for spikes

---

## ✨ Features

- 🎓 Answers grounded in expert leadership content  
- ⚡️ Fast semantic search using FAISS  
- 🗨 Conversational memory (limited context)  
- 🎨 Elegant and modern UI with smooth interactions  
- 🌐 Easily deployable with minimal configuration

---

## 🙌 Acknowledgements

This project was developed as part of a **leadership and AI exploration initiative**, combining cutting-edge LLMs with real-world content to produce useful, educational conversations.

---
