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


start = time()
for url_ in urls:
    request_function(url_)
print(f"Duration (synchronous): {time() - start}")


