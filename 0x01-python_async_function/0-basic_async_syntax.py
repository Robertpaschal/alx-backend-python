#!/usr/bin/env python3
"""This module contains an asynchronous coroutine that takes in an
integer argument with a default value, wais for some seconds and
eventually returns it"""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine that waits for a random delay between 0 and max_delay (inclusive)
    seconds and eventually returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
