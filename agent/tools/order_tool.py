from langchain.tools import tool
import json

with open(r"C:\Users\ASUS\SRICHERAN\Subjects\6TH SEMESTER\Ericsson\ecommerce_chatbot\data\orders.json") as f:
    orders_db = json.load(f)

@tool
def check_order_status(data: str) -> str:
    """Check status,location,product_name,product_type,product_category of a customer's order. Input: 'email|order_id'"""
    try:
        email, order_id = data.strip().split("|")
        order_id = int(order_id)
        customer_orders = orders_db.get(email.lower())
    except Exception:
        return "Invalid input. Use format: 'email|order_id'."
    
    if not customer_orders:
        return f"No orders found for {email}."

    order = next((o for o in customer_orders if o["order_id"] == order_id), None)
    if not order:
        return f"No order with ID {order_id} found for {email}."

    return (
        f"Order {order_id} ({order['product_name']} - {order['product_type']} - {order['product_category']}) "
        f"is currently {order['status']} and delivery location is at {order['location']}."
    )

@tool
def cancel_order(data: str) -> str:
    """Cancel a customer's order. Input: 'email|order_id'"""
    try:
        email, order_id = data.strip().split("|")
        order_id = int(order_id)
        customer_orders = orders_db.get(email.lower())
    except Exception:
        return "Invalid input. Use format: 'email|order_id'."

    if not customer_orders:
        return f"No orders found for {email}."

    order = next((o for o in customer_orders if o["order_id"] == order_id), None)
    if not order:
        return f"No order with ID {order_id} found for {email}."

    if not order["can_cancel"]:
        return f"Order {order_id} ({order['product_name']}) cannot be canceled as it's already {order['status']}."

    order["status"] = "canceled"
    return f"Order {order_id} ({order['product_name']}) has been successfully canceled and a refund will be processed."

@tool
def process_return_or_refund(data: str) -> str:
    """Initiate a return or refund. Input: 'email|order_id'"""
    try:
        email, order_id = data.strip().split("|")
        order_id = int(order_id)
        customer_orders = orders_db.get(email.lower())
    except Exception:
        return "Invalid input. Use format: 'email|order_id'."

    if not customer_orders:
        return f"No orders found for {email}."

    order = next((o for o in customer_orders if o["order_id"] == order_id), None)
    if not order:
        return f"No order with ID {order_id} found for {email}."

    if order["status"] != "delivered":
        return f"Order {order_id} hasn't been delivered yet and cannot be returned or refunded."

    if order["can_return"] and not order["can_refund"]:
        order["status"] = "exchange"
        return f"Order {order_id} is not elligible for return and will be exchanged as per policy."
    elif order["can_refund"]:
        order["status"] = "refunded"
        return f"Order {order_id} refund has been initiated."
    else:
        return f"Order {order_id} is not eligible for return or refund."
