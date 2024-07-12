import streamlit as st
from components.chat import versobot
from utils.session import initialize_session_states, chat_button, reset_chat
from utils.config import set_up_page
from versobot.components.prompt_tips import get_prompt_tips

# Language-specific strings
LANG_STRINGS = {
    "English": {
        "sidebar_text": "**Versobot** is running on OpenAI's GPT-4o. Use the button below to reset the chat.",
        "chat_button_text": "Clear Chat",
        "initial_message": "Hi, I'm **Versobot!** How can I help?",
        "placeholder": "Chat with Versobot",
        "assistant_id": "asst_i5ylsjPx1CWwe0xJFOOQ80yC",
        "prompt_tips_button": "Get Prompt Tips",
        "prompt_tips_header": "Prompt Improvement Tips:",
        "no_prompt_message": "No prompt available. Please enter a prompt in the chat first."
    },
    "Deutsch": {
        "sidebar_text": "**Versobot** läuft auf OpenAIs GPT-4o. Setzen Sie den Chat mit dem untenstehenden Button zurück.",
        "chat_button_text": "Chat löschen",
        "initial_message": "Hallo, ich bin **Versobot!** Wie kann ich helfen?",
        "placeholder": "Mit Versobot chatten",
        "assistant_id": "asst_uXO7y5oCdYpj2RlxWC2tiRP6",
        "prompt_tips_button": "Prompting-Tipps",
        "prompt_tips_header": "Tipps zur Verbesserung des Prompts:",
        "no_prompt_message": "Kein Prompt verfügbar. Bitte geben Sie zuerst einen Prompt im Chat ein."
    }
}

# App setup
set_up_page("Chat")
initialize_session_states()
st.session_state.chat = True  # Start chat by default

# Initialize session state for the latest user prompt
if 'latest_user_prompt' not in st.session_state:
    st.session_state.latest_user_prompt = ""

# Sidebar with reset button and prompt tips
with st.sidebar:
    lang = st.selectbox("Language",
                        options=list(LANG_STRINGS.keys()),
                        index=0,  # Set to English by default
                        label_visibility="collapsed",
                        on_change=reset_chat)
    st.markdown(LANG_STRINGS[lang]["sidebar_text"])
    
    # Create placeholders for the button and prompt tips
    button_placeholder = st.empty()
    tips_placeholder = st.empty()
    
    # Always show the "Clear Chat" button
    if chat_button(button_placeholder,
                   LANG_STRINGS[lang]["chat_button_text"],
                   primary=True):
        reset_chat()
        st.rerun()
    
    # Add button for prompt tips
    if st.button(LANG_STRINGS[lang]["prompt_tips_button"]):
        if st.session_state.latest_user_prompt:
            tips = get_prompt_tips(st.session_state.latest_user_prompt, lang)
            tips_placeholder.markdown(LANG_STRINGS[lang]["prompt_tips_header"])
            tips_placeholder.write(tips)
        else:
            tips_placeholder.write(LANG_STRINGS[lang]["no_prompt_message"])

# Chat interface
versobot(
    assistant_id=LANG_STRINGS[lang]["assistant_id"],
    initial_message=LANG_STRINGS[lang]["initial_message"],
    placeholder=LANG_STRINGS[lang]["placeholder"]
)