from langchain_community.tools.tavily_search import TavilySearchResults


def web_search(query):
    """ Searches for latest news of stock"""
    search = TavilySearchResults()
    res = search.run(f"{query}")
    return res
