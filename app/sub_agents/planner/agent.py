# sub_agents/planner/agent.py

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
# Ensure relative paths are correct
from ..data_collector.agent import data_collector_agent
from ..consolidated_writer.agent import consolidated_writer_agent 

stock_analysis_planner = Agent(
    name="stock_analysis_planner",
    model="gemini-2.0-flash",
    description="Orchestrates the 2-step workflow: get data, then write report.",
    instruction="""
    You are a stock analysis report planner.
    Your task is to generate a report by calling a sequence of agents.
    You must call them in this exact order:

    1.  `data_collector_agent` (To get all financial data)
    2.  `consolidated_writer_agent` (To analyze all data and write the final report)

    CRITICAL RULE: Your final response must be *the verbatim output* from the 
    `consolidated_writer_agent`. Do not add any conversational text, summaries, 
    preliminary greetings, or introductory phrases (like "Here is a stock analysis..."). 
    Your output MUST START directly with the Markdown heading: '## Stock Analysis Report: [Ticker]'.
    """,
    tools=[
        AgentTool(data_collector_agent),
        AgentTool(consolidated_writer_agent),
    ],
)