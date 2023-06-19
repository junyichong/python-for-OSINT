from duckduckgo_search import DDGS

keywords = 'osint'

with DDGS() as ddgs:
    for r in ddgs.text(keywords, region='us-en', safesearch='Off', timelimit='y'):
        print(r)