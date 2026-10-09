import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Groq ChatBot", page_icon="🤖", layout="centered")

st.title("🤖 Q&A ChatBot")
st.caption("Powered by Groq · `openai/gpt-oss-120b` · LangSmith Tracing")

# ─── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    groq_api_key = st.text_input(
        "Groq API Key",
        value=os.getenv("GROQ_API_KEY", ""),
        type="password",
        help="Auto-loaded from .env"
    )
    model_name = st.selectbox(
        "Model",
        options=["openai/gpt-oss-120b", "llama-3.3-70b-versatile", "mixtral-8x7b-32768"],
        index=0
    )
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# ─── Session State ─────────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ─── Prompt ────────────────────────────────────────────────────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and friendly AI assistant. Answer questions clearly and concisely."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

# ─── Display Chat History ──────────────────────────────────────────────────────
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# ─── Chat Input ────────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask me anything...")

if user_input:
    if not groq_api_key:
        st.error("⚠️ Please provide a Groq API Key in the sidebar or `.env` file.")
    else:
        # Show user message
        with st.chat_message("user"):
            st.write(user_input)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    model = ChatGroq(api_key=groq_api_key, model=model_name)
                    chain = prompt | model | StrOutputParser()

                    response = chain.invoke({
                        "question": user_input,
                        "chat_history": st.session_state.chat_history
                    })

                    st.write(response)

                    # Update chat history
                    st.session_state.chat_history.append(HumanMessage(content=user_input))
                    st.session_state.chat_history.append(AIMessage(content=response))

                except Exception as e:
                    st.error(f"Error: {e}")