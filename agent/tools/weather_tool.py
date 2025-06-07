from langchain.tools import tool
import random

@tool
def get_weather(city: str) -> str:
    """retrieve the current weather conditions at a customer's shipping or delivery location, and use that information to adjust or estimate the shipping time and for recommandation use weather_based_recommandation """
    weather = random.choice(['sunny','rainy','cloudy','normal'])
    return f"The current weather in {city} is {weather}."

@tool
def weather_based_recommendation(city: str) -> str:
    """Recommending products based on current weather in the city. Weather based products categories are 'skincare' or 'appliances' based on weather select these product categories, and recommand"""
    weather = random.choice(['sunny','rainy','cloudy','normal'])
    return f"The current weather in {city} is {weather}."
    