import streamlit as st

st.expander("Disclaimer", expanded=True).markdown(
    """
🔴 IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalized advice.
"""
)


# from utils.vector_store import load_and_index_documents

# # Optional: show this only for devs
# with st.sidebar.expander("🛠️ Developer Tools", expanded=False):
#     if st.button("🔄 Rebuild Vector Store"):
#         with st.spinner("Re-indexing MOM documents..."):
#             load_and_index_documents()
#         st.success("✅ Vector store rebuilt successfully!")
