import streamlit as st

from versobot_asst import versobot


# Constants
PAGE_CONFIG = {
    "page_title": "Summarization Exercise • Versobot",
    "page_icon": "assets/verso_icon.png",
    "layout": "wide",
    "initial_sidebar_state": "collapsed",
}

SOURCE_TEXTS = [
    {
        "title": "Attention Is All You Need",
        "caption": "The research paper that introduced the machine learning model architecture behind ChatGPT and others. [Read the document](https://arxiv.org/html/1706.03762v7). :blue-background[5,824 words]",
        "assistant": "asst_vfC9bLBbNehj55nMvDfxyU70"
    },
    {
        "title": "Fauci interview transcript",
        "caption": "Dr. Anthony Fauci's ten-hour closed-door testimony in front of the COVID Select Subcommittee in January 2024. [Read the document](https://oversight.house.gov/wp-content/uploads/2024/05/Fauci-Part-1-Transcript.pdf). :blue-background[58,893 words]",
        "assistant": "asst_Wspuondg32w51y2RfGOImVcf"
    },
    {
        "title": "NHTSA 2022 crash data",
        "caption": "A representative sample of 2022 U.S. vehicle collisions from the National Highway and Transit Safety Administration. [Read about the data](https://www.nhtsa.gov/crash-data-systems/crash-report-sampling-system). :blue-background[53,955 records]",
        "assistant": "asst_0kwV7wS4CrsVFksneHZbhTgF"
    }
]

SOURCE_TEXT_OPTIONS = [text["title"] for text in SOURCE_TEXTS]
SOURCE_TEXT_CAPTIONS = [text["caption"] for text in SOURCE_TEXTS]
ASSISTANTS = {text["title"]: text["assistant"] for text in SOURCE_TEXTS}


# Functions
def initialize_session_states():
    if 'chat' not in st.session_state:
        st.session_state.chat = False

    if 'source_text' not in st.session_state:
        st.session_state.source_text = None

    if 'initial_state' not in st.session_state:
        st.session_state.initial_state = []


def chat_button(button_placeholder, text, key=None, primary=False):
    return button_placeholder.button(text,
                                     type="primary" if primary else "secondary",
                                     key=key)


def reset_chat():
    st.session_state.chat = False
    st.session_state.initial_state = st.session_state.chat_history = []

# Set up Streamlit app
initialize_session_states()
st.set_page_config(**PAGE_CONFIG)
st.logo("assets/verso_logo.png", icon_image="assets/verso_icon.png")

# Page content
'''
# Exercise 1: Summarization and synthesis

#### Get what you need out of a long or complex document.

1. Choose one of the following source texts.
'''

st.session_state.source_text = st.radio(
    label="Choose a source text",
    options=SOURCE_TEXT_OPTIONS,
    index=None,
    on_change=reset_chat,
    captions=SOURCE_TEXT_CAPTIONS,
    label_visibility="collapsed")

# Show step 2 when source text is selected
if st.session_state.source_text:
    '''
    2. Use the text box below to ask me to summarize the text. Remember to be as specific as possible.

        Here are some questions to consider.

        - What are the first questions you might use to probe an unfamiliar document?
        - How do you want to receive the information you're looking for? A summary, a list of key points, a table, a chart…?
        - What questions can get you interesting information that you don't know to ask for?

    When you're ready, press :gray-background[Start Chat]. If you want to start over, choose a new source text or use the :red-background[Clear Chat] button.
    '''
    # Create a placeholder for the button
    button_placeholder = st.empty()
    
    if not st.session_state.chat:
        if chat_button(button_placeholder, "Start Chat", key="start_chat"):
            st.session_state.chat = True
    
# Chat interface
if st.session_state.chat:
    if chat_button(button_placeholder, "Clear Chat", primary=True):
        reset_chat()
        st.rerun()
    else:
        st.divider()
        versobot(assistant_id=ASSISTANTS[st.session_state.source_text],
                 initial_message=f"Hi, I'm Versobot! I'm ready to answer your questions about **{st.session_state.source_text}.**")
