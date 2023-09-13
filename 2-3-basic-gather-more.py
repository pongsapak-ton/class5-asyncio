import asyncio
import time 




async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")


async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

# Wed Sep 13 05:17:46 2023 hello 0 started
# Wed Sep 13 05:17:46 2023 hello 1 started
# Wed Sep 13 05:17:46 2023 hello 2 started
# Wed Sep 13 05:17:46 2023 hello 3 started
# Wed Sep 13 05:17:46 2023 hello 4 started
# Wed Sep 13 05:17:46 2023 hello 5 started
# Wed Sep 13 05:17:46 2023 hello 6 started
# Wed Sep 13 05:17:46 2023 hello 7 started
# Wed Sep 13 05:17:46 2023 hello 8 started
# Wed Sep 13 05:17:46 2023 hello 9 started
# Wed Sep 13 05:17:50 2023 hello 0 done
# Wed Sep 13 05:17:50 2023 hello 1 done
# Wed Sep 13 05:17:50 2023 hello 2 done
# Wed Sep 13 05:17:50 2023 hello 3 done
# Wed Sep 13 05:17:50 2023 hello 4 done
# Wed Sep 13 05:17:50 2023 hello 5 done
# Wed Sep 13 05:17:50 2023 hello 6 done
# Wed Sep 13 05:17:50 2023 hello 7 done
# Wed Sep 13 05:17:50 2023 hello 8 done
# Wed Sep 13 05:17:50 2023 hello 9 done
# Time: 4.01 sec