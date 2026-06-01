import asyncio
import time

#* 1. asyncio.gather
async def call_openai_api():
    await asyncio.sleep(1)
    print(f"OpenAI responded at {time.time():.2f}s")
    return "OpenAI API called"

async def call_groq_api():
    await asyncio.sleep(2)
    print(f"Groq responded at {time.time():.2f}s")
    return "Groq API called"

async def main():
    start=time.time()
    results=await asyncio.gather(call_openai_api(), call_groq_api())

    for result in results:
        print(f"Result: {result}")
    print(f"Total time:{time.time()-start:.2f}s")

# asyncio.run(main())


#* 2. asyncio.wait_for() -> To set a timeout for a coroutine. If coroutine does not complete within the timeout it raises a TimeoutError. -> To implement fallback functionalities

async def main_fallback():
    start=time.time()
    try:
       result=await asyncio.wait_for(call_openai_api(), timeout=0.5)
       print("Result: ", result)
    except asyncio.TimeoutError:
        print("OpenAI timed out")
        result=await call_groq_api()
        print("Fallback result: ", result)
        
    print(f"Total time:{time.time()-start:.2f}s")

# asyncio.run(main_fallback())


#* 3. async generator -> To generate a stream of data asynchronously. Useful for processing data chunk by chunk(LLM responses, real time data processing)

async def text_stream():
    text="Capital of Denmark is Copenhagen"
    for word in text.split():
        await asyncio.sleep(0.3)
        yield word

async def main_stream():
    async for word in text_stream():
        print(word, end=" ")
        print()

asyncio.run(main_stream())