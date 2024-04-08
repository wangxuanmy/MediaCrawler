import re
import httpx
from typing import Callable, Dict, List, Optional



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

path = '/user/profile/'+"65a4e46d0000000003025cfd"
response = httpx.get(f"https://www.xiaohongshu.com{path}", headers=headers)
content = response.text

print(content)
match = re.search(r'<script>window.__INITIAL_STATE__=(.+)<\/script>', content, re.M)