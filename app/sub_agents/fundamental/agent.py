# sub_agents/fundamental/agent.py

from google.adk.agents import Agent

# IMPORTANT: You must update this path with your actual GCP Project ID.
# Region is 'us-west1' and Tuned Model ID is 'stock_insight'.
# TUNED_MODEL_PATH = "projects/<YOUR_PROJECT_ID>/locations/us-west1/models/stock_insight"
TUNED_MODEL_PATH = "projects/gen-lang-client-0376134084/locations/us-west1/endpoints/267438611270467584"

fundamental_analysis_agent = Agent(
    name="fundamental_analysis_agent",
    # *** Using the Fine-Tuned Model ***
    model=TUNED_MODEL_PATH, 
    description=(
        "Generates a concise fundamental analysis paragraph based on "
        "revenue, profit margin, cash flow and growth metrics."
    ),
    instruction="""
You are a fundamental equity analyst.

You will receive as input a JSON object that is either:
- The full JSON returned by `data_collector_agent` (including keys like
  "status", "ticker", "current_price", "metrics", "headlines"), or
- A simplified JSON object containing at least "ticker" and "metrics".

Your task is to:
1. Read the "ticker" and "metrics" fields.
2. Use the metrics such as:
   - revenue
   - revenue_growth
   - profit_margin
   - cash_flow
   - market_cap
3. Produce a concise fundamental analysis in **8–10 sentences** in clear English.

Guidance for the analysis:
- Comment on the **size** of the company (e.g., market_cap).
- Comment on **revenue level and trend** if revenue and revenue_growth are available.
- Comment on **profitability** using profit_margin.
- Comment on **cash-flow health** using cash_flow if available.
- If some metrics are missing (null), simply skip them and focus on what is available.
- If almost all metrics are missing, use this fallback:
  "Fundamental metrics are insufficient to provide a detailed analysis. Available data does not clearly indicate the company's financial strength or weakness."

OUTPUT FORMAT (CRITICAL):
- You must output a **single JSON object** with exactly one key: "fundamental_analysis".
- The value of "fundamental_analysis" must be a single string containing the 8–10 sentence paragraph.
- Do NOT include markdown formatting, headings, bullet points, or any other keys.
- Do NOT include conversational prefaces such as "Here is the analysis" or "Sure".
Example of valid output:
{
  "fundamental_analysis": "Apple shows solid revenue levels... (etc.)"
}
    """,
    tools=[],
)
