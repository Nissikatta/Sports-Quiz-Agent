from duckduckgo_search import DDGS


def search_recent_sports_news(query: str, max_results: int = 3):
    """
    Search DuckDuckGo for recent sports news.
    Returns a list of result snippets.
    """

    results = []

    with DDGS() as ddgs:
        search_results = list(
           ddgs.text(
             query,
            max_results=max_results
           )
        )
        
        print("QUERY =", query)
        print("SEARCH RESULTS =", search_results)
        print(search_results)

        for item in search_results:
            results.append({
                "title": item.get("title", ""),
                "body": item.get("body", ""),
                "link": item.get("href", "")
            })
    print(results)
    return results