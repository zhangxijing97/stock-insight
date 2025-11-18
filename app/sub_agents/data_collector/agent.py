from google.adk.agents import Agent
from ...tools.financial_tools import get_stock_price, get_financial_metrics, get_market_news

data_collector_agent = Agent(
    name="data_collector_agent",
    model="gemini-2.0-flash",
    description="Extracts a ticker from a query, then fetches stock price, financial metrics, and news.",
    instruction="""
    You are a data collection agent.
    The user will provide a query, like "get an analysis of Apple" or "report for GOOGL".
    
    Your FIRST task is to *extract the company name or ticker symbol* from the query.
    If it's a company name (e.g., "Apple", "Google", "Microsoft"), 
    you must determine its stock ticker (e.g., "AAPL", "GOOGL", "MSFT").

    Once you have the ticker:
    You MUST use the available tools to fetch all required information:
    1. `get_stock_price(ticker=THE_TICKER)`
    2. `get_financial_metrics(ticker=THE_TICKER)`
    3. `get_market_news(ticker=THE_TICKER)`

    Consolidate all data from these tools into a single, structured JSON response.
    If you cannot determine a ticker from the query, respond with an error: 
    "Error: Could not determine a stock ticker from the request."
    """,
    tools=[
        get_stock_price,
        get_financial_metrics,
        get_market_news,
    ],
)