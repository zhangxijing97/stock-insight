import yfinance as yf
from typing import List, Dict, Any

def get_stock_price(ticker: str) -> Dict[str, Any]:
    """
    Gets the current stock price and currency for a given ticker.
    
    Args:
        ticker: The stock symbol (e.g., "AAPL", "GOOGL").

    Returns:
        A dictionary with ticker, current price, and currency.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        price = info.get('currentPrice', info.get('regularMarketPrice'))
        
        if not price:
            return {"status": "error", "error_message": f"Could not find price for {ticker}"}

        return {
            "status": "success",
            "ticker": ticker,
            "price": price,
            "currency": info.get('currency', 'USD')
        }
    except Exception as e:
        return {"status": "error", "error_message": f"Error fetching price for {ticker}: {str(e)}"}

def get_financial_metrics(ticker: str) -> Dict[str, Any]:
    """
    Gets key financial metrics for a ticker.
    This provides data for Fundamental and Valuation agents.
    
    Args:
        ticker: The stock symbol.

    Returns:
        A dictionary of key financial metrics.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Helper to safely get data
        def _get(key, default="N/A"):
            return info.get(key, default)

        metrics = {
            "ticker": ticker,
            "revenue": _get('totalRevenue'),
            "revenue_growth": _get('revenueGrowth'), # For fundamental
            "profit_margin": _get('profitMargins'),  # For fundamental
            "cash_flow": _get('operatingCashflow'), # For fundamental
            "pe_ratio": _get('trailingPE'),          # For valuation
            "ps_ratio": _get('priceToSales'),        # For valuation
            "forward_pe": _get('forwardPE'),
            "market_cap": _get('marketCap')
        }
        
        if metrics["revenue"] == "N/A":
             return {"status": "error", "error_message": f"No financial metrics found for {ticker}."}

        return {"status": "success", "metrics": metrics}

    except Exception as e:
        return {"status": "error", "error_message": f"Error fetching metrics for {ticker}: {str(e)}"}

def get_market_news(ticker: str) -> Dict[str, Any]:
    """
    Gets recent news headlines for a given ticker.
    
    Args:
        ticker: The stock symbol.

    Returns:
        A dictionary containing a list of news headlines.
    """
    try:
        stock = yf.Ticker(ticker)
        news = stock.news
        
        if not news:
            return {"status": "success", "headlines": ["No recent news found."]}
        
        # Extract just the titles
        headlines = [item.get('title') for item in news if item.get('title')]
        
        return {
            "status": "success",
            "headlines": headlines[:5] # Return top 5
        }
    except Exception as e:
        return {"status": "error", "error_message": f"Error fetching news for {ticker}: {str(e)}"}