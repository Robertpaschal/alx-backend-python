#!/usr/bin/env python3
"""
This module provides coroutine to generate and collect random
numbers asynchronously
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator using an
    asynchronous comprehension, and returns the list of these numbers.
    """
    return[numbers async for numbers in async_generator()]
