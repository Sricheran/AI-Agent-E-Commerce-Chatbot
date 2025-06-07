from langchain.tools import tool
import json

with open(r"C:\Users\ASUS\SRICHERAN\Subjects\6TH SEMESTER\Ericsson\ecommerce_chatbot\data\products_category.json") as f:
    product_categories_db = json.load(f)

with open(r"C:\Users\ASUS\SRICHERAN\Subjects\6TH SEMESTER\Ericsson\ecommerce_chatbot\data\products_details.json") as f:
    product_details_db = json.load(f)

with open(r"C:\Users\ASUS\SRICHERAN\Subjects\6TH SEMESTER\Ericsson\ecommerce_chatbot\data\products_info.json") as f:
    product_info = json.load(f)



@tool
def search_products(category_or_name: str) -> str:
    """Search and get products by category or product type. Input should be in singular format eg: laptop, not laptops"""
    cat = category_or_name.lower()
    if cat in product_categories_db:
        items = product_categories_db[cat]
        return f"Category '{cat}' includes: {', '.join(items)}."
    elif cat in product_details_db:
        products = product_details_db[cat]
        return f"Product type '{cat}' includes: {', '.join(products)}."
    elif cat in product_info:
        result=get_product_details(cat)
        return result
    else:
        return f"No products found under '{category_or_name}'."

@tool
def get_product_details(product_name: str) -> str:
    """Get price and availability for a specific product variant."""
    name = product_name.strip()
    info = product_info.get(name)
    if not info:
        return f"No details found for product '{name}'."
    return f"{name} costs INR {info['price']} and is currently {info['availability']}."

@tool
def recommend_products(query: str) -> str:
    """Recommend products (only if you know the prefernce of customeror else ignore this) based on a user query or interest. input should be only 'product name', or 'category name'.Input should be in singular format eg: laptop, not laptops"""
    interest = query.lower()

    recommendations = []
    for category, types in product_categories_db.items():
        if interest in category or interest in types:
            for ptype in types:
                recommendations.extend(product_details_db.get(ptype, []))

    if not recommendations:
        return f"No recommendations found based on '{query}'."
    
    return f"Based on your interest in '{query}', we recommend: {', '.join(recommendations[:5])}."
