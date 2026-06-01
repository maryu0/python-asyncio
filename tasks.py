import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data...")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

#* Using create_task to run multiple coroutines concurrently
#* We can even alter the await order of tasks if we want some tasks to complete before others(Lines: 14,15,18)
async def main():
    task1=asyncio.create_task(fetch_data(1,2))
    task2=asyncio.create_task(fetch_data(2,3))

    # result1=await task1
    # result2=await task2
    task3=asyncio.create_task(fetch_data(3,4))

    # result3=await task3
    result1=await task1
    result2=await task2
    result3=await task3

    print(result1,result2,result3)

asyncio.run(main())