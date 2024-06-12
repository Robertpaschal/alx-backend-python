#!/usr/bin/env python3
"""This module provides a coroutine that generates random numbers."""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yeilds a random number between 0 and 10, ten times,
    with a 1-second delay between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
    