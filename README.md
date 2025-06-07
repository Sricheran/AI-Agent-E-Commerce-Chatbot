# AI-Agent-E-Commerce-Chatbot

An intelligent, autonomous customer support chatbot built for e-commerce platforms. This assistant is capable of understanding and fulfilling user queries by accessing customer, product, and order data, while also interfacing with external tools like weather APIs to provide contextual support.

---

## 🚀 Overview

**Shoppie Assistant** is a LangChain-powered chatbot designed to simulate a smart customer support agent. It can:

- Handle customer inquiries end-to-end
- Access order data and take actions (e.g., cancel, refund)
- Provide real-time product and delivery info
- Make personalized product recommendations
- Adjust responses based on external conditions like weather

---

## 🧰 Tech Stack

- **Python**
- **LangChain**
- **Groq (llama3-8b-8192 via OpenAI-compatible API)**
- **Streamlit** (UI)
- **python-dotenv** (env config)
- **JSON** (data storage)

---

## 🔐 Functional Modules

### 🔑 Login & Session Control
- First screen accepts **user email** for login.
- `st.session_state` used to:
  - Track logged-in user
  - Manage conversation memory and navigation

---

### 💬 Customer Query Chatbot

**Agent Type**: `ZERO_SHOT_REACT_DESCRIPTION`  
**LLM**: `llama3-8b-8192` via Groq API  
**Framework**: LangChain

#### ✅ Supported Query Types:
- Order tracking, cancellation, return, refund
- Product detail search and availability checks
- Personalized product recommendations
- Weather-aware delivery advice

---

## 🛠️ Tools Integrated

### 📦 Order Tool
- Source: `orders.json`
- Features:
  - `check_order_status`
  - `cancel_order`
  - `process_return_or_refund`
- Email-based access control ensures security

---

### 🛍️ Product Tool
- Sources:
  - `products.json` (types)
  - `categories.json` (categories)
  - `info.json` (availability, pricing)
- Functions:
  - `search_products`
  - `get_product_details`
  - `recommend_products` (contextual, preference-based)

---

### 👤 Customer Preferences Tool
- Source: `customers.json`
- Functions:
  - `get_customer_info`
  - `update_preferences`
  - `check_loyalty_points`
- Supports:
  - Profile info access
  - Preference-based personalization

---

### 🌦️ Weather Tool
- Simulated weather responses by location
- Features:
  - `get_weather`
  - `weather_based_recommendation`
- Influences delivery and product suggestions

---

## 🧠 LangChain Agent Configuration

Agent Type: ZERO_SHOT_REACT_DESCRIPTION
LLM: llama3-8b-8192 via Groq API
### Tools: 
- check_order_status
- cancel_order
- process_return_or_refund
- search_products
- get_product_details
- recommend_products
- get_customer_info
- update_preferences
- check_loyalty_points
- get_weather
- weather_based_recommendation


## 💻 UI Flow (via Streamlit)

- **Login Page**:  
  Enter email to begin a personalized session.

- **Home Dashboard**:  
  Explore product categories, detailed product listings, and general shopping info.

- **Profile**:  
  View your name, registered email, and loyalty points.

- **Orders**:  
  Track current orders, check status, and request cancellations, returns, or refunds.

- **Chatbot**:  
  Interact with the AI assistant to get instant help through natural language queries.

---

## 📁 Data Files

- `orders.json`
- `customers.json`
- `products_category.json`
- `products_details.json`
- `products_info.json`

---

## 📌 Note

This is a **prototype project** developed for educational and demonstration purposes.  
All data used in this application is simulated and not connected to any real users or products.

---

## 📬 Contributor

Developed by **SriCheran CH**  
