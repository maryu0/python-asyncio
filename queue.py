import asyncio

#* Queue handles "burst": if 20 task arrive at once, and we want to process only 5 tasks at a time, the other task will wait in the queue

async def producer(queue):
    for i in range(5):
        await queue.put(f"request_{i}")  #* producer adds item in the queue
        print(f"Added request {i}")
        await asyncio.sleep(0.5)

async def consumer(queue):
    while True:
        item=await queue.get()           #* consumer gets item from the queue; waits if empty
        print(f"Processing {item}")
        queue.task_done()                #* mark an item as processed
    
async def main():
    queue=asyncio.Queue()                #* create a queue
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())