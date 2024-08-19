#!/usr/bin/env pyhton3
"""
Write a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """
    args: list[int]
    Returns: float
    """
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
