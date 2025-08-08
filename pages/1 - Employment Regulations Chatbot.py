import streamlit as st

from openai import OpenAI
from dotenv import load_dotenv

from utils.utility import check_password
from utils.agent import run_agent


# region &lt;--------- Streamlit Page Configuration ---------&gt;
st.set_page_config(layout="centered", page_title="My Streamlit App - Page 1")

# Do not continue if check_password is not True.
# if not check_password():
#     st.stop()

# Show title and description.
st.title("💬 Employment Regulations")
st.write("This is a chatbot to ask about employment regulations in Singapore. ")
# endregion &lt;--------- Streamlit Page Configuration ---------&gt;


# the API key will be loaded from .env and available in os.environ
load_dotenv()

CHROMA_PATH = "../data/chroma_store"

# create a session state variable to store the chat messages
# this ensures that the messages persist across reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# create a chat input field to allow the user to enter a message
if prompt := st.chat_input("What would you like to enquire today?"):

    # store and display the current prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # run the agent with the prompt
    response = run_agent(prompt)

    # Stream the response to the chat using `st.write_stream`, then store it in
    # session state.
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
