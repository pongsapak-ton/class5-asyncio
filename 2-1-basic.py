import asyncio
import time


async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")


async def main():
    # returns immediately,  the task is created
    task1 = asyncio.create_task(hello(1))
    # await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

#     Wed Sep 13 05:19:50 2023 hello 1 started
# Wed Sep 13 05:19:50 2023 hello 2 started
# Wed Sep 13 05:19:54 2023 hello 1 done
# Wed Sep 13 05:19:54 2023 hello 2 done
# Time: 4.01 sec