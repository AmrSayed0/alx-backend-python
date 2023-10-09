#!/usr/bin/env python3

import asyncio
import random

# Asynchronous coroutine that takes an integer argument 'max_delay'
# with a default value of 10 and returns a random delay between 0 and max_delay seconds.
async def wait_random(max_delay: int = 10) -> float:
    # Generate a random float value between 0 and max_delay (inclusive).
    delay = random.uniform(0, max_delay)
    
    # Asynchronously wait for the generated delay.
    await asyncio.sleep(delay)
    
    # Return the random delay.
    return delay