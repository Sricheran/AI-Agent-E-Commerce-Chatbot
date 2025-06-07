from agent.agent_builder import get_agent
import warnings
warnings.filterwarnings('ignore')

agent = get_agent()

email="jane@example.com"

query="Cancel my laptop order and request for refund"

prompt = f"""
Customer email: {email}
Query: {query}

Instructions:
- Use ONLY relevant tools to answer the question.
- Before making decisions, always retrieve customer info
- Chain tools when strictly needed
- Don't use tools unnecessarily. If a direct answer is possible, do so.
- Recommandation of products is striclty done only when asked in query.
- If any data (like order ID or product name) is missing, infer context or summarize response dont loop or continue answer.
- Be specific, concise, and user-friendly.
- Based on customer query searches on products, update their prefernces and recommend products accordingly.
- If action is 'None' or If Missing 'Action:' after 'Thought', summarise and get to final answer.
"""

response = agent.run(prompt)
print("\nAgent Response:", response)
