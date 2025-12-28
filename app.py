
import streamlit as st
from config.settings import Settings
from salvin_assi.gemini_engine import GeminiEngine
from salvin_assi.prompt_controller import PromptController
from salvin_assi.memory import Memory
from salvin_assi.assistant import SalvinAssistant

st.set_page_config(page_title="SALVIN", layout="centered")
st.title("🧠 SALVIN Your Personal AI Assistant")

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

theme_toggle = st.sidebar.toggle("🌙 Dark Mode", value=True)

role = st.sidebar.selectbox(
    "Select Assistant Role",
    ["Tutor", "Coding Assistant", "Career Mentor"]
)

if st.sidebar.button("🧹 Clear Memory"):
    Memory().clear()
    st.session_state.chat = [] 
    st.sidebar.success("Memory cleared!")


settings = Settings()
engine = GeminiEngine(settings.load_api_key())
memory = Memory()
prompt_controller = PromptController(role)
salvin = SalvinAssistant(engine, prompt_controller, memory)



if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Ask SALVIN...")

if user_input:
    response = salvin.respond(user_input)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("SALVIN", response))

for speaker, msg in st.session_state.chat:
    with st.chat_message("assistant" if speaker == "SALVIN" else "user"):
        st.write(msg)
        
st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        color: #FF6363;
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #212121;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] * {
        color: #26CCC2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    """
    <style>
    .typing-container {
        font-family: monospace;
        color: #26CCC2;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .typing-line {
        white-space: nowrap;
        overflow: hidden;
        width: 0;
        animation: typing 1.2s steps(var(--chars)) forwards;
        margin-bottom: 4px;
    }

    .line1 { --chars: 6; animation-delay: 0s; }
    .line2 { --chars: 7; animation-delay: 1.3s; }
    .line3 { --chars: 11; animation-delay: 2.7s; }

    @keyframes typing {
        from { width: 0; }
        to { width: calc(var(--chars) * 1ch); }
    }
    </style>

    <div class="typing-container">
        <div class="typing-line line1">SALVIN</div>
        <div class="typing-line line2">Is Here</div>
        <div class="typing-line line3">To Help You</div>
    </div>
    """,
    unsafe_allow_html=True
)


st.session_state.theme = "dark" if theme_toggle else "light"
if st.session_state.theme == "dark":
    st.markdown("""
    <style>
    .stApp {
        background-color: #161b22;
        color: #ffffff;
        
    }
    section[data-testid="stSidebar"] {
        background-color: #161b22;
    }
       /* USER chat bubble */
    div[data-testid="stChatMessage"][aria-label="user"] {
        background-color: #2563eb;
        color: white;
        border-radius: 12px;
        padding: 10px;
    }

    /* ASSISTANT chat bubble */
    div[data-testid="stChatMessage"][aria-label="assistant"] {
        background-color: #1f2933;
        color: #e5e7eb;
        border-radius: 12px;
        padding: 10px;
    }

    /* Chat text */
    div[data-testid="stChatMessage"] * {
        color: inherit !important;
    }
    </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <style>
    .stApp {
        background-color: white;
        color: #000000;
    }
    section[data-testid="stSidebar"] {
        background-color: #EFFFFD;
    }
    </style>
    """, unsafe_allow_html=True)
    
st.sidebar.markdown("""
<style>
.wave {
  display: flex;
  gap: 4px;
  margin-top: 10px;
}
.wave span {
  width: 4px;
  height: 20px;
  background: #26CCC2;
  animation: wave 1.2s infinite ease-in-out;
}
.wave span:nth-child(2) { animation-delay: -1.1s; }
.wave span:nth-child(3) { animation-delay: -1.0s; }
.wave span:nth-child(4) { animation-delay: -0.9s; }
.wave span:nth-child(5) { animation-delay: -0.8s; }

@keyframes wave {
  0%, 40%, 100% { transform: scaleY(0.3); }
  20% { transform: scaleY(1); }
}
</style>

<div class="wave">
  <span></span><span></span><span></span><span></span><span></span>
</div>
<p style="color:#26CCC2;font-size:12px;">I'm hearing you, ask query </p>
""", unsafe_allow_html=True)
