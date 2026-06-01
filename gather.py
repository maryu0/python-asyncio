import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data...")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

#* Using gather() to run multiple coroutines and collect their results. DOES NOT HAVE ERROR HANDLING
# async def main():
#     results=await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))

#     for result in results:
#         print(f"Result: {result}")


#* For ERROR HANDLING we use TaskGroup()
async def main():
    tasks=[]
    async with asyncio.TaskGroup() as tg:
        for i,sleep_time in enumerate([2,1,3], start=1):
            task=tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)


    results=[task.result() for task in tasks]
    for result in results:
        print(f"Result: {result}")


asyncio.run(main())