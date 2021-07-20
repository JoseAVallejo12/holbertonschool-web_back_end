#!/usr/bin/env python3
"""Annotate the below function’s parameters and return appropriate types"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function

    Args:
        lst (Iterable[Sequence]): arg

    Returns:
        List[Tuple[Sequence, int]]: return
    """
    return [(i, len(i)) for i in lst]
