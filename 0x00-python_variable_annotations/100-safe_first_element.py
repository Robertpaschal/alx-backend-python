#!/usr/bin/env python3
"""This module contains a function whihc returns the first element
of an iterable or non if the iterable is empty"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of an iterable or None if the iterable is empty.

    Args:
        lst (Iterable[Any]): An iterable of elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence, or
        None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
