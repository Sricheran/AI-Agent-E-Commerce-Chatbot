import streamlit as st
import json
from agent.agent_builder import get_agent

with open("data/products_category.json") as f:
    categories = json.load(f)

with open("data/products_details.json") as f:
    product_details = json.load(f)

with open("data/products_info.json") as f:
    product_info = json.load(f)

with open("data/customers.json") as f:
    customers = json.load(f)

with open("data/orders.json") as f:
    orders_data = json.load(f)

st.set_page_config(page_title="Shoppie Assistant", layout="wide")

if 'email' not in st.session_state:
    st.session_state.email = None
if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'agent' not in st.session_state:
    st.session_state.agent = get_agent()

def nav_button(label, target):
    if st.sidebar.button(label):
        st.session_state.page = target
        st.rerun()

def sidebar_nav():
    st.sidebar.title("🔍 Navigation")
    nav_button("🏠 Home", "home")
    nav_button("👤 Profile", "profile")
    nav_button("📦 My Orders", "orders")
    nav_button("🤖 Chatbot", "chatbot")
    nav_button("🚪 Logout", "login")

if st.session_state.page == 'login':
    st.markdown("<h1 style='text-align: center;'>🛍️ Welcome to Sample Shoppie!</h1>", unsafe_allow_html=True)
    email = st.text_input("📧 Enter your email to login:")

    if st.button("Continue") and email:
        email = email.strip().lower()
        st.session_state.email = email
        st.session_state.page = 'home'
        st.rerun()

else:
    sidebar_nav()

    if st.session_state.page == 'home':
        st.title("🛍️ Product Showcase")

        st.subheader("📚 Categories")
        st.markdown(f"**Available Categories:** {', '.join(categories)}")

        st.subheader("🧾 Product Details")
        for item, types in product_details.items():
            with st.expander(f"🛒 {item}"):
                st.write(types)

        st.subheader("ℹ️ General Information")
        for info, types in product_info.items():
            with st.expander(f"📌 {info}"):
                st.write(types)

    elif st.session_state.page == 'profile':
        user = customers.get(st.session_state.email)
        st.title("👤 User Profile")
        if user:
            st.markdown(f"**Name:** {user['name']}")
            st.markdown(f"**Email:** {st.session_state.email}")
            st.markdown(f"**Loyalty Points:** 🏆 {user['loyalty_points']}")
        else:
            st.warning("🚫 You are a new user.")

    elif st.session_state.page == 'orders':
        st.title("📦 My Orders")
        email = st.session_state.email
        orders = orders_data.get(email, [])

        if not orders:
            st.warning("🚫 You have no orders yet.")
        else:
            for order in orders:
                with st.expander(f"📦 Order #{order['order_id']} - {order['product_name']}"):
                    st.write(f"**Category:** {order['product_category'].capitalize()}")
                    st.write(f"**Type:** {order['product_type'].capitalize()}")
                    st.write(f"**Status:** `{order['status'].upper()}`")
                    st.write(f"**Location:** {order['location'].title()}")
                    st.write(f"**Cancelable:** {'✅' if order['can_cancel'] else '❌'}")
                    st.write(f"**Refundable:** {'✅' if order['can_refund'] else '❌'}")
                    st.write(f"**Returnable:** {'✅' if order['can_return'] else '❌'}")

    elif st.session_state.page == 'chatbot':
        st.title("🤖 Chat with ShopAgent")

        for user_msg, bot_msg in st.session_state.chat_history:
            st.markdown(f"**🧑 You**: {user_msg}")
            st.markdown(f"**🤖 Agent**: {bot_msg}")

        query = st.text_input("💬 Type your query:", key="chat_input")

        if st.button("Send") and query:
            prompt = f"""
            Customer email: {st.session_state.email}
            Query: {query}

            Instructions:
            - Use ONLY relevant tools to answer the question.
            - Before making decisions, always retrieve customer info. If customer info is not available, ignore retriving customer info, and get to the query and come to final answer.
            - Chain tools when strictly needed
            - Don't use tools unnecessarily. If a direct answer is possible, do so.
            - Recommandation of products is striclty done only when asked in query.
            - If any data (like order ID or product name) is missing, infer context or summarize response dont loop or continue answer.
            - Be specific, concise, and user-friendly.
            - Based on customer query searches on products, update their prefernces and recommend products accordingly.
            - If action is 'None' or If Missing 'Action:' after 'Thought', summarise and get to final answer.
            """

            with st.spinner("💡 Thinking..."):
                response = st.session_state.agent.run(prompt)

            st.session_state.chat_history.append((query, response))
            st.rerun()
