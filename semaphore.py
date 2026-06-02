import asyncio
import random

#* Semaphore limits the number of concurrent access to a resource; in this case, we want to limit the number of concurrent API calls to 3

sem=asyncio.Semaphore(3)                                #* allow at most 3 concurrent calls

async def call_api(i: int):
    async with sem:                                      #* acquire the semaphore 
        print(f"[start] request {i}")
        await asyncio.sleep(random.uniform(0.5,1.5))     #* simulating API call time
        print(f"[end] request {i}")

async def main():
    task=[asyncio.create_task(call_api(i)) for i in range(10)]
    await asyncio.gather(*task)

asyncio.run(main())