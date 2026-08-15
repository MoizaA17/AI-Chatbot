# 🤖 AI Chatbot with Memory

A simple conversational chatbot built with **Streamlit** and **Google's Gemini API** that remembers previous messages in the conversation.

---

## 📖 What it does

This app is a chat interface where you type messages and get responses from Google's Gemini model. Unlike a basic single-turn chatbot, it keeps track of the conversation history in the session, so the model has context from earlier messages when generating replies.

---

## ✨ Key features

- 🧠 **Conversational memory** across turns — previous messages are passed back to the model as context
- 💬 **Chat-style UI** built with Streamlit's `st.chat_message` and `st.chat_input` components
- ⚡ **Powered by Google Gemini API** via the `google-genai` SDK
- 🛡️ Basic error handling for failed API calls
- 🔐 API key kept out of source code using environment variables

---

## 🛠️ Tech stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core language |
| 🎈 Streamlit | UI framework |
| ✨ Google Gemini API (`google-genai`) | Language model |
| 🔑 python-dotenv | Environment variable management |

---

## 🚀 Setup / Installation

These steps assume you have Python installed but nothing else set up.

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install streamlit python-dotenv google-genai
```
(Or, if you have a `requirements.txt` in the repo: `pip install -r requirements.txt`)

### 4️⃣ Get a Gemini API key
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey) 🔗
- Sign in and generate an API key
- Copy the key

### 5️⃣ Set up your environment variables
- In the project root, create a file named `.env`
- Add your API key to it:
  ```
  GEMINI_API_KEY=your_api_key_here
  ```
---

## ▶️ How to run it locally

From the project folder, with your virtual environment activated:

```bash
streamlit run Chatbot.py
```

This will open the app in your browser 🌐, usually at `http://localhost:8501`.

---

## 📸 Screenshots

*Screenshots of the chat interface go here.*

Suggested setup:
- Create a `screenshots/` folder in the repo root
- Save your image(s) there, e.g. `screenshots/chat-example.png`
- Reference them in this README like:
  ```markdown
  ![Chat interface](screenshots/chat-example.png)
  ```

---

## ⚠️ Known limitations

Being upfront here — this is a learning project, not a polished product:

- 🩹 **Error handling is basic** — API failures are caught and shown as a generic error message in the UI, but there's no retry logic, input validation, or more specific handling for different failure types (rate limits, invalid API key, network issues, etc.)
- 💾 **No persistent memory** — conversation history lives only in Streamlit's session state, so it's lost when the app restarts or the session ends
- 📏 **No handling for long conversations** — could eventually hit the model's context limits
- 👥 **Not built for multi-user/public deployment** — no authentication or rate-limiting on the app itself

---

## 🔭 What I'd improve next

- 🎯 More specific error handling (network errors vs. invalid API key vs. rate limits)
- 🗄️ Persist conversation history to a file or database so it survives restarts
- 🧹 Add a "clear conversation" button
- ✅ Add basic input validation/sanitization
- 🌊 Stream responses for a more responsive feel

---

## 📝 Note

This is a learning project built to understand how to combine Streamlit with the Gemini API and manage conversational state — not a production-ready application. 🙂
