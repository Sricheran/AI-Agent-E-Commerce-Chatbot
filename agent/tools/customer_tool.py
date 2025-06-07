from langchain.tools import tool
import json

with open(r"C:\Users\ASUS\SRICHERAN\Subjects\6TH SEMESTER\Ericsson\ecommerce_chatbot\data\customers.json") as f:
    customers = json.load(f)

@tool
def get_customer_info(email: str) -> str:
    """Retrieve customer's name, loyality points, prefernces, and order history (only order ids) from the database."""
    email=email.strip()
    user = customers.get(email.lower())
    if not user:
        return "Customer not found."
    prefs = ", ".join(user["preferences"])
    order_ids=", ".join(user["order_ids"])
    return f"Customer {user['name']} has {user['loyalty_points']} loyalty points and preferences: {prefs} and he has orders with order ids {order_ids}"

@tool
def update_preferences(data: str) -> str:
    """Update preferences using input format 'email|preference'. Udate this based on customer query and product searches in queries"""
    try:
        email, preference = data.strip().split("|")
        user = customers.get(email.lower())
    except Exception:
        return "Invalid input. Please use format: 'email|preference'."
    if not user:
            return "Customer not found."
    if preference in user["preferences"]:
            return f"Preference '{preference}' is already present for {user['name']}."
    user["preferences"].append(preference)
    return f"Preference '{preference}' added for {user['name']}."

@tool
def check_loyalty_points(email: str) -> str:
    """Check loyalty points using customer email."""
    email=email.strip()
    user = customers.get(email.lower())
    if not user:
        return "Customer not found."
    return f"{user['name']} has {user['loyalty_points']} loyalty points."
