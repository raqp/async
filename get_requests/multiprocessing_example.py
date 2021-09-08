from concurrent.futures import ProcessPoolExecutor
from time import time
import requests


urls = ["https://www.google.com",
        "https://www.python.org/",
        "https://www.list.am/",
        "https://medium.com/",
        "https://stackoverflow.com/"]


def request_function(url):
    response = requests.get(url)
    print(response.status_code, url)


def main():
    start = time()
    with ProcessPoolExecutor(max_workers=8) as executor:
        for url_ in urls:
            executor.submit(request_function, url_)
    print(f"Duration (multiprocessing): {time() - start}")


if __name__ == '__main__':
    main()


