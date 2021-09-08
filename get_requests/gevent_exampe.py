import gevent
from gevent import monkey

monkey.patch_all()
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


jobs = []
for i in urls:
    jobs.append(gevent.spawn(request_function, i))

start = time()
gevent.joinall(jobs)
print(f"Duration (gevent): {time() - start}")


