from concurrent.futures import ProcessPoolExecutor
from time import time

NUMBER = 500000000


def calculate(n):
    while n > 0:
        n -= 1


def main(n):
    start = time()
    with ProcessPoolExecutor(max_workers=n) as executor:
        for _ in range(n):
            executor.submit(calculate, NUMBER // n)
    print(f"Duration (multiprocessing): {time() - start}")


if __name__ == '__main__':
    main(4)



