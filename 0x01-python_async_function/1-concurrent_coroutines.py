#!/usr/bin/env python3
"""
This module executes multiple coroutines with async
"""
from typing import Coroutine, List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that spawns wait_random n times
    with the specified max_delay.
    Collects all delays and returns them in ascending order
    without using sort().
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
