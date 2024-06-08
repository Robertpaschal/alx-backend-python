#!/usr/bin/env python3
"""
This module contains a type-annotated function that takesa float and
returns a function that multiplies a float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates and returns s function that
    multiplies a float by the given multiplier
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
