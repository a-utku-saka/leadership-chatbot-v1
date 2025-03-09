from flask import Flask, render_template, request, jsonify
from modules.chatbot import chat_with_gpt

app = Flask(__name__)

@app.route("/")
def index():
    """Return the main UI page."""
    return render_template("index.html")  # render the templates/index.html file

@app.route("/chat", methods=["POST"])
def chat():
    """Flask API that returns a response to a question from the user."""
    data = request.json
    user_query = data.get("question", "")
    chat_history = data.get("history", [])  # Chat history from the user

    if not user_query:
        return jsonify({"error": "Lütfen bir soru girin."}), 400

    #  Create the chat 
    answer = chat_with_gpt(user_query, chat_history)

    return jsonify({"answer": answer, "history": chat_history})  # return the chat history

if __name__ == "__main__":
    app.run(debug=True)
