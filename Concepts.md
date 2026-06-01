# AsyncIO Concepts — From Basics to Generators

## What is `asyncio`?

`asyncio` is Python's built-in library for writing concurrent programs using `async` and `await` [1]. It is mainly useful for **I/O-bound** work such as API calls, database queries, network requests, sockets, and streaming, where a program spends time waiting for external systems instead of using the CPU heavily [1][2].

In simple words, `asyncio` helps one thread handle multiple waiting tasks efficiently by switching to other work whenever a task is blocked on I/O [2]. This is why it is so common in modern Python web frameworks and API clients [1].

## Why use `asyncio`?

The main reason to use `asyncio` is that waiting time can be reused. If one API request is waiting for a server response, the event loop can run another coroutine instead of leaving the program idle [2][3].

Typical use cases:

- Calling multiple APIs concurrently [1]
- Building web backends such as FastAPI apps that handle many requests efficiently [4][1]
- Streaming responses chunk by chunk [4][5]
- Queues, background work, and rate-limited request handling [1][3]

## I/O-bound vs CPU-bound

`asyncio` is best for **I/O-bound** tasks, where most of the time is spent waiting for something external such as disk, network, or database access [2][1]. It is generally **not** the right tool for CPU-heavy work like large numerical computation, image processing, or model training, because those tasks keep the CPU busy instead of yielding control [2].

Rule of thumb:

- Use `asyncio` for waiting-heavy tasks.
- Use multiprocessing, worker systems, or optimized native libraries for CPU-heavy tasks.

## Event loop

The **event loop** is the core engine of `asyncio`. It runs tasks, pauses them when they hit an `await`, and resumes them when the awaited operation is ready [2][1].

A useful mental model is: the event loop is like a scheduler managing many tasks cooperatively. A task runs until it reaches a point where it says, "I need to wait," and then the loop gives another task a turn [2].

## Coroutine

A **coroutine** is a function declared with `async def` [3]. Calling it does **not** execute it immediately; it creates a coroutine object that must be awaited or scheduled to actually run [3].

Example:

```python
import asyncio

async def say_hi():
    await asyncio.sleep(1)
    return "hi"
```

Important ideas:

- `async def` creates a coroutine function [3]
- Calling it returns a coroutine object [3]
- `await` runs another awaitable and pauses the current coroutine until it finishes [2][3]

## `await`

`await` can be used inside an `async def` function to pause the current coroutine until another awaitable completes [3]. While that coroutine is paused, the event loop can continue running other tasks [2].

This is the key reason async code is efficient for network-heavy applications. Instead of blocking the whole program, the current coroutine simply gives control back to the event loop [2][1].

## Running async code

A common entry point is `asyncio.run()`, which creates an event loop, runs the top-level coroutine, and closes the loop when finished [1].

Example:

```python
import asyncio

async def main():
    await asyncio.sleep(1)
    print("done")

asyncio.run(main())
```

## Concurrency with `asyncio.gather`

`asyncio.gather()` runs multiple awaitables concurrently and waits for all of them to complete [3]. This is useful when several independent API calls can happen at the same time.

Example:

```python
import asyncio

async def a():
    await asyncio.sleep(1)
    return "A"

async def b():
    await asyncio.sleep(2)
    return "B"

async def main():
    results = await asyncio.gather(a(), b())
    print(results)
```

If task `a()` takes 1 second and task `b()` takes 2 seconds, total runtime is about 2 seconds, not 3, because they are running concurrently under the event loop [3].

## Task

A **Task** is how `asyncio` schedules a coroutine to run on the event loop [3]. Creating a task tells the event loop, "start managing this coroutine independently."

Common way to create one:

```python
task = asyncio.create_task(my_coroutine())
```

Tasks are useful when work should begin in the background while other async code continues [3]. They are the main building block for concurrent workflow in real applications.

## `asyncio.wait_for`

`asyncio.wait_for()` adds a timeout around an awaitable [3]. If the operation does not finish in time, `asyncio.TimeoutError` is raised [3].

Example:

```python
import asyncio

async def slow_call():
    await asyncio.sleep(3)
    return "done"

async def main():
    try:
        result = await asyncio.wait_for(slow_call(), timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print("timed out")
```

This is especially useful for API fallback logic, where one provider should be abandoned if it is too slow [3].

## Queue idea in async systems

An `asyncio.Queue` is a coordination structure where producers put items in and consumers process them asynchronously [1]. It is useful when requests arrive faster than they should be processed, or when work should be buffered and handled in order.

Main operations:

- `await queue.put(item)` to add work
- `await queue.get()` to receive work
- `queue.task_done()` to mark completion

This becomes very relevant in systems involving request queues, worker pipelines, or backpressure management [1].

## Why generators matter before async generators

A **generator** is a function that yields values one at a time using `yield`, instead of returning everything at once [6][7]. It remembers its state between yields, so it can pause and resume later [8][9].

This matters because async generators build directly on this same idea: produce values gradually over time rather than all at once [10][5].

## Normal function vs generator

Normal function:

```python
def get_numbers():
    return [1, 2, 3]
```

Generator:

```python
def get_numbers():
    yield 1
    yield 2
    yield 3
```

Difference:

- A normal function computes the full result and returns once.
- A generator produces one value at a time on demand [7][11].
- A generator pauses at each `yield` and resumes from that exact point later [8][9].

## Why use generators?

Generators are useful when values should be produced lazily rather than stored all at once [12][13]. This improves memory efficiency and fits naturally with streaming-style workflows [12][14].

Common uses:

- Reading huge files line by line [13][14]
- Producing sequences incrementally [6]
- Streaming chunks of output instead of building everything first [15][5]

## `yield`

The `yield` keyword turns a function into a generator [7][11]. When Python hits `yield`, it returns that value to the caller and saves the function's execution state so it can continue later from the same spot [6][7].

Example:

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

Use it like this:

```python
for x in count_up_to(3):
    print(x)
```

## Generator mental model

A generator is best thought of as a **resumable iterator-producing function** [8][9]. Each iteration asks the generator for the next value, and the generator continues from where it last paused.

That is why generators are perfect preparation for async streaming. Instead of producing all output immediately, they release values step by step.

## Async generator

An **async generator** is defined with `async def` and uses `yield` inside it [10][5]. It can both `await` and `yield`, which makes it ideal for streaming values that arrive over time.

Example:

```python
import asyncio

async def stream_words():
    for word in ["The", "capital", "of", "France", "is", "Paris"]:
        await asyncio.sleep(0.3)
        yield word
```

You consume an async generator with `async for` [5]:

```python
async def main():
    async for word in stream_words():
        print(word, end=" ")
```

This pattern is highly relevant in FastAPI and LLM apps because a response can be sent chunk by chunk as pieces become available [4][15][5].

## What to remember

- `asyncio` is for concurrent **I/O-bound** programming with `async` and `await` [2][1].
- The **event loop** schedules and resumes tasks cooperatively [2].
- A **coroutine** is created with `async def` and usually runs through `await` [3].
- `asyncio.gather()` runs multiple awaitables concurrently [3].
- `asyncio.wait_for()` adds timeout control [3].
- A **generator** uses `yield` to produce values one at a time [6][7].
- An **async generator** combines `await` and `yield` for streaming async data [10][5].
