#!/usr/bin/env python3
"""hat takes a string k and an int OR float v as arguments and returns a tuple.
    The first element of the tuple is the string k. The second element is the
    square of the int/float v and should be annotated as a float."""

from typing import Iterable, List, Union, Tuple


def to_kv(k: str,  v: Union[int, float]) -> Tuple[str, float]:
    """function

    Args:
        k (str): arg one
        v (Union[int, float]): arg two

    Returns:
        Tuple[str, float]: return
    """
    return (k, float(v))
