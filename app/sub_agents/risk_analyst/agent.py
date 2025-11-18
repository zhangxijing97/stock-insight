from google.adk.agents import Agent

risk_analyst_agent = Agent(
    name="risk_analyst_agent",
    model="gemini-2.0-flash",
    description="Analyzes news and financial data to output structured risk analysis.",
    instruction="""
    You are a meticulous risk analyst.
    Look at the previous turn in the conversation for the output
    from the `data_collector_agent`.

    Find the news 'headlines' from that data.
    Your task is to identify and list the top 3-5 potential risks 
    based *only* on those headlines.
    
    Format your output as a simple, structured list.
    
    If the data is not available or reports an error, 
    you must respond with "Risk analysis is not available."
    """,
    tools=[], 
)