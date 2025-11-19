# root_agent.py

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# Import the planner for the slow path
from .sub_agents.planner.agent import stock_analysis_planner

# Import get_stock_price for the fast path
from .tools.financial_tools import get_stock_price

# This is the top-level agent.
root_agent = Agent(
    name="stock_insight_core",
    model="gemini-2.0-flash", 
    description="Core agent of Stock Insight: routes financial queries for fast price lookup or comprehensive analysis reports.",
    instruction="""
    You are the core agent of Stock Insight — a financial assistant.
    Your job is to route the user's request to the correct tool.

    -   If the user asks for a 'full analysis', 'report', 'deep dive', 
        or 'complete overview' of a stock, you *must* use the 
        `stock_analysis_planner` tool.
        
    -   If the user *only* asks for the current 'price' or 'cost' 
        of a stock, use the `get_stock_price` tool.

    -   If the query is ambiguous, ask for clarification: 
        "Are you looking for just the current price or a full analysis report?"
    """,
    tools=[
        get_stock_price, # For simple price requests
        AgentTool(stock_analysis_planner), # For full analysis reports
    ],
)