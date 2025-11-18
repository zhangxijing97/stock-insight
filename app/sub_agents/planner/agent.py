from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
# 确保相对路径正确
from ..data_collector.agent import data_collector_agent
from ..fundamental_analyst.agent import fundamental_analyst_agent
from ..risk_analyst.agent import risk_analyst_agent
from ..valuation_analyst.agent import valuation_analyst_agent
from ..final_writer.agent import final_writer_agent

stock_analysis_planner = Agent(
    name="stock_analysis_planner",
    model="gemini-2.0-flash",
    description="Orchestrates a 5-step workflow (data, fundamental, risk, valuation, writer) to produce a stock analysis report.",
    instruction="""
    You are a stock analysis report planner.
    Your task is to generate a report by calling a sequence of agents.
    You must call them in this exact order:

    1.  `data_collector_agent` (To get all financial data)
    2.  `fundamental_analyst_agent` (To analyze the data)
    3.  `risk_analyst_agent` (To analyze the data)
    4.  `valuation_analyst_agent` (To analyze the data)
    5.  `final_writer_agent` (To assemble the final report)

    Your final response to the user must be *only* the output
    from the `final_writer_agent`. Do not add any other text or summary.
    """,
    tools=[
        AgentTool(data_collector_agent),
        AgentTool(fundamental_analyst_agent),
        AgentTool(risk_analyst_agent),
        AgentTool(valuation_analyst_agent),
        AgentTool(final_writer_agent),
    ],
)