import streamlit as st
from components.chat import versobot
from utils.session import initialize_session_states, chat_button, reset_chat
from utils.config import set_up_page

# Language-specific strings
LANG_STRINGS = {
    "English": {
        "sidebar_text": """
        :gray-background[**Versobot**] is running on OpenAI's GPT-4o.
        
        Click the **✕** above to collapse this sidebar, or reset the chat with the button below.
        """,
        "chat_button_text": "Clear Chat",
        "initial_message": "Hi, I'm **Versobot!** How can I help?",
        "placeholder": "Chat with Versobot",
        "assistant_id": "asst_i5ylsjPx1CWwe0xJFOOQ80yC"
    },
    "Deutsch": {
        "sidebar_text": """
        :gray-background[**Versobot**] läuft auf OpenAIs GPT-4o.
        
        Klicken Sie auf das **✕** oben, um diese Seitenleiste zu minimieren, oder setzen Sie den Chat mit dem untenstehenden Button zurück.
        """,
        "chat_button_text": "Chat löschen",
        "initial_message": "Hallo, ich bin **Versobot!** Wie kann ich helfen?",
        "placeholder": "Mit Versobot chatten",
        "assistant_id": "asst_uXO7y5oCdYpj2RlxWC2tiRP6"
    }
}

# App setup
set_up_page("Chat")
initialize_session_states()
st.session_state.chat = True  # Start chat by default

# Sidebar with reset button
with st.sidebar:
    lang = st.selectbox("Language",
                        options=list(LANG_STRINGS.keys()),
                        index=1,
                        label_visibility="collapsed",
                        on_change=reset_chat)
    LANG_STRINGS[lang]["sidebar_text"]
    button_placeholder = st.empty()

# Chat interface
if chat_button(button_placeholder,
               LANG_STRINGS[lang]["chat_button_text"],
               primary=True):
    reset_chat()
    st.rerun()
else:
    versobot(
        assistant_id=LANG_STRINGS[lang]["assistant_id"],
        initial_message=LANG_STRINGS[lang]["initial_message"],
        placeholder=LANG_STRINGS[lang]["placeholder"]
    )
