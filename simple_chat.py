import streamlit as st
from components.chat import versobot
from utils.session import initialize_session_states, chat_button, reset_chat
from utils.config import set_up_page


# App setup
set_up_page("Chat")
initialize_session_states()
st.session_state.chat = True  # Start chat by default

# Sidebar with reset button
with st.sidebar:
    """
    :gray-background[**Versobot**] is running on OpenAI's GPT-4o.
    
    Click the **✕** above to collapse this sidebar, or reset the chat with the button below.
    """
    button_placeholder = st.empty()

# Chat interface
if chat_button(button_placeholder, "Clear Chat", primary=True):
    reset_chat()
    st.rerun()
else:
    versobot(assistant_id="asst_i5ylsjPx1CWwe0xJFOOQ80yC",
                initial_message="Hi, I'm **Versobot!** How can I help?")
