from time import time

NUMBER = 500000000


def calculate(n):
    while n > 0:
        n -= 1


def main():
    start = time()
    calculate(NUMBER)
    print(f"Duration (synchronous): {time() - start}")


if __name__ == '__main__':
    main()

