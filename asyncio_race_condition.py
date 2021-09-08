import asyncio
from random import randint

counter = 0


async def update():
    global counter

    current_counter = counter
    await asyncio.sleep(randint(0, 1))
    counter = current_counter + 1


event_loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(update()) for _ in range(10)]
event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()

print(counter)
