import time
import asyncio

async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")


async def main():
    task1 = asyncio.create_task(hello(1))
    # await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

# Wed Sep 13 05:19:21 2023 hello 1 started
# Wed Sep 13 05:19:21 2023 hello 2 started
# Wed Sep 13 05:19:25 2023 hello 1 done
# Wed Sep 13 05:19:25 2023 hello 2 done
# Time: 4.01 sec