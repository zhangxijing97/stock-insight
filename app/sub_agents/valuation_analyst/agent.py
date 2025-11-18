from google.adk.agents import Agent

valuation_analyst_agent = Agent(
    name="valuation_analyst_agent",
    model="gemini-2.0-flash",
    description="Analyzes valuation metrics (PE, PS, forward PE) to explain if a stock is 'expensive' or 'cheap'.",
    instruction="""
    You are a valuation analyst.
    Look at the previous turn in the conversation for the output
    from the `data_collector_agent`.

    Find the valuation metrics (e.g., pe_ratio, ps_ratio, forward_pe)
    from that data's 'metrics' section.
    
    Your task is to write a concise paragraph (3-5 sentences) 
    explaining whether the stock appears 'expensive', 'cheap', or 
    'fairly valued' based *only* on those metrics.
    
    If the data is not available or reports an error, 
    you must respond with "Valuation analysis is not available."
    """,
    tools=[], 
)