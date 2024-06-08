#!/usr/bin/env python3
from typing import List
"""
This module contains a type-annotated function sum_list
which takes a list input_list of floats as argument and
returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """
    Sums a list of floating point numbers and returns the result"""
    return sum(input_list)
