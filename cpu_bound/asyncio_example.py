import asyncio
from time import time

NUMBER = 500000000


async def calculate(n):
    while n > 0:
        n -= 1


def main(n):
    event_loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(calculate(NUMBER // n)) for _ in range(n)]
    start = time()
    event_loop.run_until_complete(asyncio.gather(*tasks))
    print(f"Duration (asyncio): {time() - start}")


if __name__ == '__main__':
    main(4)
