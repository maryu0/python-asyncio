# Python AsyncIO Concepts

This folder contains concept-focused examples for learning Python asyncio.

The goal is to build intuition for:

- Coroutines
- Tasks and concurrent execution
- gather and TaskGroup patterns
- Timeouts and fallback handling
- Locks and shared resource protection
- Async generators and streaming-style output

## Folder Purpose

This is a practice and reference folder for understanding how asynchronous programming works in Python for I/O-heavy workflows.

## Files Included

- Concepts.md: Notes and explanations from basics to advanced ideas.
- coroutine.py: Basic coroutine creation and awaiting.
- Need_for_TASKS.py: Why plain awaiting can run sequentially and why tasks are needed for concurrency.
- tasks.py: Using create_task to run multiple coroutines concurrently.
- gather.py: Running multiple coroutines with gather and using TaskGroup for safer handling.
- Lock.py: Protecting shared state with asyncio.Lock.
- Practice.py: Practical patterns including gather, wait_for fallback, and async generator streaming.
- queue.py: Producer/consumer example using `asyncio.Queue` to handle bursts and buffering.
- semaphore.py: Concurrency-limiting example using `asyncio.Semaphore` to throttle simultaneous calls.

## How To Run

From this folder, run any file with Python:

python coroutine.py
python Need_for_TASKS.py
python tasks.py
python gather.py
python Lock.py
python Practice.py
python queue.py
python semaphore.py

## Recommended Learning Order

1. coroutine.py
2. Need_for_TASKS.py
3. tasks.py
4. gather.py
5. Lock.py
6. Practice.py
7. queue.py
8. semaphore.py
9. Concepts.md

## Audience

This folder is useful for beginners and intermediate Python learners who want hands-on asyncio understanding before using frameworks or production systems.

## Notes

- These examples are intentionally small and educational.
- Focus is on clarity and asyncio concepts, not production architecture.
- New examples `queue.py` and `semaphore.py` demonstrate queue buffering and concurrency throttling patterns.
