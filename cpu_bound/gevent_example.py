import gevent
from time import time

NUMBER = 500000000


def calculate(n):
    while n > 0:
        n -= 1


def main(n):
    jobs = [gevent.spawn(calculate, NUMBER // n) for _ in range(n)]
    start = time()
    gevent.joinall(jobs)
    print(f"Duration (gevent): {time() - start}")


if __name__ == '__main__':
    main(4)
