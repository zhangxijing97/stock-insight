from google.adk.agents import Agent

fundamental_analyst_agent = Agent(
    name="fundamental_analyst_agent",
    model="gemini-2.0-flash",
    description="Analyzes financial metrics (revenue, margin, cash flow) to produce a fundamental analysis paragraph.",
    instruction="""
    You are a senior fundamental financial analyst.
    Look at the previous turn in the conversation for the output
    from the `data_collector_agent`.
    
    Find the financial metrics (e.g., revenue, profit_margin, cash_flow, revenue_growth)
    from that data's 'metrics' section.
    
    Your task is to write a concise, professional paragraph (3-5 sentences) 
    analyzing *only* these fundamentals.
    
    If the data is not available or reports an error, 
    you must respond with "Fundamental analysis is not available."
    """,
    tools=[], 
)