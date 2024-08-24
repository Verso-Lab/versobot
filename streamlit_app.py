import streamlit as st
from utils.config import set_up_page

pg = st.navigation([
    st.Page("pages/prompting_tips.py", title="Prompting tips", icon=":material/forum:"),
    st.Page("pages/summarization.py", title="Summarization [buggy]", icon=":material/summarize:")
])
pg.run()
