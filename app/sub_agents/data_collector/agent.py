# sub_agents/data_collector/agent.py

from google.adk.agents import Agent
# Ensure relative path is correct
from ...tools.financial_tools import get_all_stock_data 

data_collector_agent = Agent(
    name="data_collector_agent",
    model="gemini-2.0-flash",
    description="Extracts a ticker from a query, then fetches all stock data in one consistent call.",
    instruction="""
    You are a data collection agent.
    The user will provide a query.
    
    Your FIRST task is to *extract the company name or ticker symbol* from the query 
    and convert it to the official ticker (e.g., "AAPL", "MSFT").

    Once you have the ticker:
    You MUST use the available tool `get_all_stock_data` once, passing the ticker.
    Do not call any other tools.

    Return the complete structured JSON response from the tool.
    """,
    tools=[
        get_all_stock_data,
    ],
)
