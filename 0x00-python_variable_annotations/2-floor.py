#!/usr/bin/env python3
"""
This module contains a type-annotated function
floor which takes a float n as argument and returns the floor of the float.
"""


def floor(n: float) -> int:
    """
    Rerurns the floor of a floating number
    """
    if n >= 0:
        return int(n)
    else:
        return int(n) - (n != int(n))
