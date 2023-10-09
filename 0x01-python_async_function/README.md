````markdown
# alx-backend-python: Asynchronous Python Functions

This repository contains Python scripts demonstrating asynchronous programming concepts. The tasks and their respective solutions are organized into different files within the `0x01-python_async_function` directory.

## Files and Tasks

### 0-basic_async_syntax.py

This file contains the implementation of asynchronous coroutines for basic asynchronous programming.

#### Task 0: The Basics of Async

Write an asynchronous coroutine `wait_random` that takes an integer argument (`max_delay`, default value: 10) and waits for a random delay between 0 and `max_delay` (inclusive) seconds before returning the delay.

Usage:

```python
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```
````

### 1-concurrent_coroutines.py

This file implements an async routine to execute multiple coroutines concurrently.

#### Task 1: Let's Execute Multiple Coroutines at the Same Time with Async

Write an async routine `wait_n` that takes two integers, `n` and `max_delay`. It spawns `wait_random` `n` times with the specified `max_delay` and returns the list of delays in ascending order.

Usage:

```python
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```

### 2-measure_runtime.py

This file measures the total execution time of concurrent coroutines.

#### Task 2: Measure the Runtime

Write a function `measure_time` that takes integers `n` and `max_delay` as arguments. It measures the total execution time for `wait_n(n, max_delay)` and returns the average time per coroutine execution.

Usage:

```python
measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9
print(measure_time(n, max_delay))
```

### 3-tasks.py

This file demonstrates the creation and usage of asyncio tasks.

#### Task 3: Tasks

Write a function `task_wait_random` that takes an integer `max_delay` and returns an asyncio.Task.

Usage:

```python
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

### 4-tasks.py

This file utilizes asyncio tasks with the modified `task_wait_n` function.

#### Task 4: Tasks

Take the code from `wait_n` and create a new function `task_wait_n`. This function is nearly identical to `wait_n`, except `task_wait_random` is being called.

Usage:

```python
import asyncio
task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```
