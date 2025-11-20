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
    description=(
        "Core agent of Stock Insight: routes financial queries either to a "
        "fast price lookup tool or to a multi-agent planner that orchestrates "
        "a full stock analysis report."
    ),
    instruction="""
You are the core agent of Stock Insight — a financial assistant.

Your job is to route the user's request to the correct tool:

- If the user asks for a 'full analysis', 'report', 'deep dive',
  'complete overview', or anything that implies a **comprehensive assessment**
  of a stock, you MUST use the `stock_analysis_planner` tool.
  The planner will orchestrate multiple expert agents to generate a full report.

- If the user ONLY asks for the current 'price', 'quote' or 'cost'
  of a single stock, use the `get_stock_price` tool.

- If the query is ambiguous, ask for clarification, such as:
  "Are you looking for just the current price or a full analysis report?"

When in doubt, prefer the full analysis planner for richer insights.
    """,
    tools=[
        get_stock_price,                  # For simple price requests
        AgentTool(stock_analysis_planner) # For full analysis reports
    ],
)


# # root_agent.py

# from google.adk.agents import Agent
# from google.adk.tools.agent_tool import AgentTool

# # --- 1. 定义 TUNED_MODEL_PATH ---
# # 确保这是你 Fine-tuned 模型的正确路径
# TUNED_MODEL_PATH = "projects/gen-lang-client-0376134084/locations/us-west1/models/stock_insight"


# # This is the TEMPORARY top-level agent for simple path testing.
# root_agent = Agent(
#     name="stock_insight_path_tester",
#     # *** 直接将 root_agent 设置为 Fine-tuned 模型 ***
#     model=TUNED_MODEL_PATH,
#     description="Temporary agent used only to test if the fine-tuned model path is functional and authenticated.",
#     instruction="""
#     You are a simple test assistant. The user will ask you a basic general knowledge question. 
#     You must answer the question using the knowledge of the model you are running.
#     Do NOT mention stock analysis or financial metrics.
#     """,
#     # 移除所有工具，只测试模型本身的能力
#     tools=[], 
# )