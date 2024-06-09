#!/usr/bin/env python3
"""
This module contains a function that uses TypeVar to annotate it's
parameter
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')
NoneType = TypeVar('NoneType', bound=None)

def safely_get_value(
        dct: Mapping,
        key: Any, default: Union[T, NoneType] = None) -> Union[Any,T]:
    """
    Safely gets a value from a dictionary by key,
    returning a default value if the key is not found.

    Args:
        dct (Dict[Any, T]): The dictionary from which to get the value.
        key (Any): The key to look for in the dictionary.
        default (Optional[T], optional): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Optional[T]: The value from the dictionary if the key is found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
