import streamlit as st
from agent.agent_builder import get_agent

st.set_page_config(page_title="E-Commerce Chatbot", layout="centered")

# Session setup
if 'email' not in st.session_state:
    st.session_state.email = None

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'agent' not in st.session_state:
    st.session_state.agent = get_agent()

if 'awaiting_response' not in st.session_state:
    st.session_state.awaiting_response = False

if 'user_input_value' not in st.session_state:
    st.session_state.user_input_value = ""

# ---------- PAGE 1: Email Entry ----------
if st.session_state.email is None:
    st.title("🛍️ E-Commerce Chatbot Login")
    email_input = st.text_input("Enter your email to begin:")

    if st.button("Start Chat") and email_input:
        st.session_state.email = email_input.strip().lower()
        st.rerun()

# ---------- PAGE 2: Chatbot ----------
else:
    st.title(f"Welcome, {st.session_state.email}")
    st.markdown("### 💬 Chat with your assistant below")

    # Display chat history
    for user_msg, bot_msg in st.session_state.chat_history:
        st.markdown(f"**You:** {user_msg}")
        st.markdown(f"**Agent:** {bot_msg}")

    # Input and submit
    query = st.text_input("Type your query and press Enter:", key="user_input", value=st.session_state.user_input_value)
    submit = st.button("Send")

    if submit and query:
        st.session_state.awaiting_response = True
        st.session_state.last_query = query

    if st.session_state.awaiting_response:
        with st.spinner("Processing..."):
            prompt = f"""
            Customer email: {st.session_state.email}
            Query: {st.session_state.last_query}

            Instructions:
            - Use ONLY relevant tools to answer the question.
            - Before making decisions, always retrieve customer info
            - Stop reasoning after Final Answer is provided. Do not loop or re-analyze.
            - Chain tools when strictly needed
            - Recommendation of products is strictly done only when asked in query and should be done checking available products.
            - If any data (like order ID or product name) is missing, infer context or summarize response, don't loop or continue answer.
            - Don't use tools unnecessarily. If a direct answer is possible, do so.
            - Be specific, concise, and user-friendly.
            - Based on customer query searches on products, update their preferences and recommend products accordingly.
            - If action is 'None' or If Missing 'Action:' after 'Thought', summarise and get to final answer.
            """
            response = st.session_state.agent.run(prompt)

        # Save chat history
        st.session_state.chat_history.append((st.session_state.last_query, response))

        # Clear input value and stop loop
        st.session_state.user_input_value = ""
        st.session_state.awaiting_response = False

        st.rerun()

    if st.button("🔄 Reset Chat"):
        st.session_state.clear()
        st.rerun()
