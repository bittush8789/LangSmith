# 🤖 Groq Q&A ChatBot with LangSmith Tracing

A simple, fast, and intelligent **Q&A ChatBot** built with **Groq**, **LangChain**, and **Streamlit** — with full observability via **LangSmith**.

---

## 🚀 Features

- 💬 **Interactive Chat UI** — Native Streamlit chat interface (`st.chat_message`)
- ⚡ **Groq Inference** — Ultra-fast responses powered by Groq's LPU hardware
- 🧠 **Conversation Memory** — Maintains full chat history across turns
- 🔍 **LangSmith Tracing** — Every chain call is automatically traced and logged
- 🔄 **Model Selection** — Switch between models from the sidebar
- 🗑️ **Clear Chat** — Reset the conversation with one click

---

## 🧱 Tech Stack

| Technology | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [LangChain](https://www.langchain.com/) | LLM chain orchestration |
| [ChatGroq](https://console.groq.com/) | LLM inference (Groq API) |
| [LangSmith](https://smith.langchain.com/) | Tracing & observability |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 📁 Project Structure

```
Langsmith/
├── app.py              # Main Streamlit ChatBot application
├── .env                # API keys (not committed to git)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── LICENSE             # License file
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Langsmith
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_TRACING_V2=true
```

#### 🔑 Where to get the API Keys:
- **Groq API Key** → [console.groq.com](https://console.groq.com) → API Keys
- **LangSmith API Key** → [smith.langchain.com](https://smith.langchain.com) → Settings → API Keys

---

## ▶️ Run the App

```bash
streamlit run app.py
```

The app will open at **http://localhost:8501** in your browser.

---

## 🖥️ Usage

1. Open the app in your browser
2. *(Optional)* Enter your **Groq API Key** in the sidebar if not set in `.env`
3. *(Optional)* Select a **model** from the sidebar dropdown
4. Type your question in the chat input box at the bottom
5. Press **Enter** to get an instant AI response
6. Use **🗑️ Clear Chat** in the sidebar to start a fresh conversation

---

## 🤖 Available Models

| Model ID | Description |
|---|---|
| `openai/gpt-oss-120b` | OpenAI GPT-OSS 120B (default) — High-capability, 131K context |
| `llama-3.3-70b-versatile` | Meta LLaMA 3.3 70B — Fast & versatile |
| `mixtral-8x7b-32768` | Mixtral 8x7B — Great for longer contexts |

---

## 📊 LangSmith Tracing

All chat interactions are automatically traced in **LangSmith** when `LANGCHAIN_TRACING_V2=true` is set.

To view traces:
1. Go to [smith.langchain.com](https://smith.langchain.com)
2. Navigate to **Projects** → `Groq-Streamlit-App`
3. Inspect individual runs, inputs, outputs, and latency

---

## 📦 requirements.txt

```
langchain
langchain_groq
langchain_core
python-dotenv
streamlit
```

---

## 📄 License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

---

## 🙌 Acknowledgements

- [Groq](https://groq.com/) for blazing-fast LLM inference
- [LangChain](https://www.langchain.com/) for the chain orchestration framework
- [Streamlit](https://streamlit.io/) for the simple and beautiful UI framework
- [LangSmith](https://smith.langchain.com/) for LLM observability