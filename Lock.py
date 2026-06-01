import asyncio

# A shared variable
shared_resource=0

# Lock to protect access to shared res
lock=asyncio.Lock()

async def modify_shared_res():
    global shared_resource
    async with lock: #*  Acquiring the lock -> ensures that that diff coroutine can not access the shared resource until the lock is released 
        # Critical section start
        print(f"Resource before mod: {shared_resource}")
        shared_resource+=1
        await asyncio.sleep(1)
        print(f"Resource after mod: {shared_resource}")
        # Critical section end

async def main():
    await asyncio.gather(*(modify_shared_res() for _ in range(5)))

asyncio.run(main())


