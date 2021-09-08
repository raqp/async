from threading import Thread
import requests
from time import time

urls = ["https://www.google.com",
        "https://www.python.org/",
        "https://www.list.am/",
        "https://medium.com/",
        "https://stackoverflow.com/"]


def request_function(url):
    response = requests.get(url)
    print(response.status_code, url)


workers = [Thread(target=request_function, args=(url,)) for url in urls]
start = time()

for worker in workers:
    worker.start()

for worker in workers:
    worker.join()

print(f"Duration (threading): {time() - start}")
