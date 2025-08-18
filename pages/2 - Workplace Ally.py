import streamlit as st

from utils.utility import check_password
from utils.agent import create_agent_ally, agent_ally_search
from utils.translate import detect_language, translate_text


# start Streamlit Page Configuration
st.set_page_config(layout="centered", page_title="My Streamlit App - Page 2")

# Do not continue if check_password is not True.
if not check_password():
    st.stop()

# Show title and description.
st.title("🤝 Workplace Ally (Multi-lingual)")
st.write(
    "Hi, I am Ally, your workplace best friend. I'll help you by listening to your concerns."
)
st.write(
    "Sample questions include:\n"
    "- I have not been paid my salary for three months. What are my rights?\n"
    "- 我的上司 经常骂我笨,然后大声喊我. 我该怎么做？\n"
    "- I am told by my boss to work 12 hours a day, without being paid Overtime. What can I do?"
)
# end Streamlit Page Configuration

# create agent once per session
if "agent" not in st.session_state:
    st.session_state.agent = create_agent_ally()

# Input
user_input = st.text_area(
    "Describe your situation below. You may type in your preferred language."
)
# lang = detect_language(user_input) if user_input else "en"

if st.button("Assist me"):
    if not user_input.strip():
        st.warning("Please write your concerns.")
        st.stop()

    with st.spinner("Detecting language..."):
        user_lang = detect_language(user_input)
    st.info(f"Detected language: {user_lang}")

    # 1) Translate to English if needed
    if user_lang != "en":
        with st.spinner("Translating to English..."):
            query_en = translate_text(user_input)
        st.info(f"Translated to English: {query_en}")
    else:
        query_en = user_input

    with st.spinner("Thinking..."):
        response = agent_ally_search(st.session_state.agent, query_en)

    if user_lang != "en":
        with st.spinner("Translating response back to your language..."):
            response = translate_text(response, target_lang=user_lang)
        # st.info(f"Response in {user_lang}: {response}")
    st.markdown(f"🤝 Ally says: {response}")
