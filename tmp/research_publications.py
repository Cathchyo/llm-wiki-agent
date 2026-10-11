import concurrent.futures
import json
import sys
import requests
from bs4 import BeautifulSoup


def fetch(url):
    try:
        response = requests.get(url, timeout=30)
        soup = BeautifulSoup(response.text, 'html.parser')
        for node in soup(['script', 'style', 'nav', 'footer']):
            node.decompose()
        content = ' '.join(soup.get_text(' ', strip=True).split())
        return {'url': url, 'status': response.status_code, 'text': content[:22000]}
    except Exception as error:
        return {'url': url, 'error': str(error)}


sys.stdout.reconfigure(encoding='utf-8')
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    for result in pool.map(fetch, sys.argv[1:]):
        print(json.dumps(result, ensure_ascii=False))
