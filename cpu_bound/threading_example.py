from threading import Thread
from time import time

NUMBER = 500000000


def calculate(n):
    while n > 0:
        n -= 1


def main(n):
    workers = [Thread(target=calculate, args=(NUMBER // n,)) for _ in range(n)]
    start = time()
    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()
    print(f"Duration (threading): {time() - start}")


if __name__ == '__main__':
    main(4)

