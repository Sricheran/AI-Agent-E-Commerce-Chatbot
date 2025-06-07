import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")  

from agent.tools.order_tool import check_order_status, cancel_order, process_return_or_refund
from agent.tools.product_tool import search_products, get_product_details, recommend_products
from agent.tools.customer_tool import get_customer_info, update_preferences, check_loyalty_points
from agent.tools.weather_tool import get_weather, weather_based_recommendation

tools = [
    check_order_status,
    cancel_order,
    process_return_or_refund,
    search_products,
    get_product_details,
    recommend_products,
    get_customer_info,
    update_preferences,
    check_loyalty_points,
    get_weather,
    weather_based_recommendation
]

def get_agent():
    llm = ChatOpenAI(
        temperature=0,
        model="llama3-8b-8192",  
        openai_api_base=os.environ["OPENAI_API_BASE"],
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        memory=memory,
        max_iterations=10
    )
    return agent
