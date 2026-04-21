def mock_search(query: str):
    query = query.lower()

    if "crypto" in query:
        return "Bitcoin hits all-time high after ETF approvals"
    elif "ai" in query:
        return "OpenAI launches new model replacing junior developers"
    elif "market" in query:
        return "Stock markets rise due to strong earnings reports"
    else:
        return "General tech news trending worldwide"
