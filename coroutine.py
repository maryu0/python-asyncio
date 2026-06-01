import asyncio


# Coroutine function
async def fetch_data(delay):
    print(f"Fetching data...")
    await asyncio.sleep(delay)
    print("Data fetched!")
    return{"data": "Sample data"}

async def main():
    print("Start of main function")
    task=fetch_data(2) # Creating a coroutine object
    #* We need to await the coroutine to execute it
    result =await task 
    print(f"Result:  {result}")
    print("End of main coroutine")


# async def main():
#     print("Start of main function")
#     task=fetch_data(2) # Creating a coroutine object
#     print("End of main coroutine")

      #! If we dont await the coroutine the fetch_data even though it is called it will not execute
#     result =await task 
#     print(f"Result:  {result}") 

# Running the main coroutine
asyncio.run(main())