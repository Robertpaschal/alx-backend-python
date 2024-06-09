#!/usr/bin/env python3
"""
This module uses mypy to validate and correct type annotations in
it's function
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in an array by repeating each element according to the given factor.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int): The zoom factor, defaults to 2.

    Returns:
        Tuple[int, ...]: A new tuple with elements repeated according to the zoom factor.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)



