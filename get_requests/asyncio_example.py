import asyncio
import aiohttp
from time import time

urls = ["https://www.google.com",
        "https://www.python.org/",
        "https://www.list.am/",
        "https://medium.com/",
        "https://stackoverflow.com/"]


async def request_function(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            print(response.status, url)


event_loop = asyncio.get_event_loop()

tasks = [asyncio.ensure_future(request_function(url)) for url in urls]

start = time()
event_loop.run_until_complete(asyncio.gather(*tasks))
print(f"Duration (asyncio): {time() - start}")
event_loop.close()
