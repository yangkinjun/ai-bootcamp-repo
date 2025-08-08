import streamlit as st
from utils.utility import check_password

# region &lt;--------- Streamlit Page Configuration ---------&gt;

st.set_page_config(
    layout="centered",
    page_title="My Streamlit App - Page 2"
)

# Do not continue if check_password is not True.  
if not check_password():  
    st.stop()

# endregion &lt;--------- Streamlit Page Configuration ---------&gt;

# st.title("🤖 Employment Regulations Chatbot")
st.title("💬 Employment Regulations Chatbot")

role = st.selectbox("Select your role:", ["Worker", "Employer/HR", "Foreign Job Seeker"])
# language = st.selectbox("Preferred language:", ["English", "Chinese", "Malay", "Tamil", "Bengali"])

user_question = st.text_input("Ask a question about your employment rights or obligations:")

# if user_question:
#     with st.spinner("Thinking..."):
#         response = answer_question(user_question, role=role, language=language)
#     st.markdown("### 🧠 AI Response:")
#     st.write(response)

# form = st.form(key="form")
# form.subheader("Prompt")

# user_prompt = form.text_area("Enter your prompt here", height=200)

# if form.form_submit_button("Submit"):
#     print(f"User has submitted {user_prompt}")


