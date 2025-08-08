import streamlit as st
from utils.utility import check_password

# region &lt;--------- Streamlit Page Configuration ---------&gt;

st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion &lt;--------- Streamlit Page Configuration ---------&gt;

# st.title("Streamlit App")
# form = st.form(key="form")
# form.subheader("Prompt")

# user_prompt = form.text_area("Enter your prompt here", height=200)

# if form.form_submit_button("Submit"):
#     print(f"User has submitted {user_prompt}")

st.title("AI-powered assistant for understanding Singapore's employment regulations")
st.markdown("""
This is your one-stop AI-powered assistant for understanding Singapore's employment regulations.

Explore key features:
- 💬 Employment Regulations Chatbot
- 📘 Employment Law Explorer
- 🛂 Work Pass Eligibility Checker
- 📄 Contract Clause Validator
- 📅 Upcoming Policy Changes
""")

# from utils.vector_store import load_and_index_documents

# # Optional: show this only for devs
# with st.sidebar.expander("🛠️ Developer Tools", expanded=False):
#     if st.button("🔄 Rebuild Vector Store"):
#         with st.spinner("Re-indexing MOM documents..."):
#             load_and_index_documents()
#         st.success("✅ Vector store rebuilt successfully!")
