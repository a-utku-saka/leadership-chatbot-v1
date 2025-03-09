let chatHistory = []; // Create array to keep chat history

function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;  // Block sending empty messages

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p class="user-message"><strong>Sen:</strong> ${userInput}</p>`;
    document.getElementById("user-input").value = "";  // Clear Input

    // Show loading animation
    let spinner = document.getElementById("loading-spinner");
    spinner.style.display = "block";

    // Add to chat history (keep limited)
    chatHistory.push({ role: "user", content: userInput });
    if (chatHistory.length > 5) chatHistory.shift(); // Just keep the last 5 messages

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userInput, history: chatHistory })
    })
    .then(response => response.json())
    .then(data => {
        console.log("API Yanıtı:", data);
        
        let botMessage = data.answer ? data.answer : data;
        chatBox.innerHTML += `<p class="bot-message"><strong>Bot:</strong> ${botMessage}</p>`;

        // add the bot's response to the chat history
        chatHistory.push({ role: "assistant", content: botMessage });
        if (chatHistory.length > 5) chatHistory.shift(); // keep the last 5 messages

        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error("Hata:", error);
        chatBox.innerHTML += `<p class="bot-message"><strong>Bot:</strong> Bir hata oluştu.</p>`;
    })
    .finally(() => {
        // Hide loading animation
        spinner.style.display = "none";
    });
}


// Send message
function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}
function closeInfoBox() {
    document.getElementById("info-box").style.display = "none";
}

// Speech-to-Text 
const micButton = document.getElementById("mic-button");

if ("SpeechRecognition" in window || "webkitSpeechRecognition" in window) {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "tr-TR"; // Turkish language support
    recognition.continuous = false; // Listening in one go
    recognition.interimResults = false; // Show provisional results

    micButton.addEventListener("click", () => {
        recognition.start();
        micButton.style.backgroundColor = "#4CAF50"; // The microphone will be green when active
    });

    recognition.onresult = (event) => {
        const text = event.results[0][0].transcript;
        document.getElementById("user-input").value = text; // Insert text in input field
        micButton.style.backgroundColor = ""; // Reset colour
    };

    recognition.onerror = (event) => {
        console.error("Ses Tanıma Hatası:", event.error);
        micButton.style.backgroundColor = ""; // Reset colour
    };

} else {
    micButton.style.display = "none"; // Hide button if browser does not support
    console.warn("Bu tarayıcı ses tanımayı desteklemiyor.");
}
