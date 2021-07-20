#!/usr/bin/env python3
"""Write a function which takes a list input_list of
    floats as argument and returns their sum as a float."""


from typing import Iterable, List


def sum_list(input_list: List[float]) -> float:
    """sum all float number in list

    Args:
        input_list (List[float]): arg

    Returns:
        float: result
    """
    return sum(input_list)
