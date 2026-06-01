import asyncio


# Coroutine function
async def fetch_data(delay,id):
    print("Fetching data... id:", id)
    await asyncio.sleep(delay)
    print("Data fetched, id", id)
    return{"data": "Sample data"}

#* In this the 1st task will execute after 2 sec and again after another 2sec the 2nd task will execute unlike what we want i.e for both of them to execute concurrently. To do this we use TASKS.
async def main():
    print("Start of main function")
    task1=fetch_data(2,1) 
    task2=fetch_data(2,2)

    result1=await task1
    print(f"Result:  {result1}")
   
    result2=await task2
    print(f"Result:  {result2}")
    

asyncio.run(main())

