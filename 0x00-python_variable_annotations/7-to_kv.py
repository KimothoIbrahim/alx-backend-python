#!/usr/bin/env python3
"""
Write a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    args: k: str
          v: int | str
    Returns: Tuple[]
    """
    return tuple([k, v**2])
    
