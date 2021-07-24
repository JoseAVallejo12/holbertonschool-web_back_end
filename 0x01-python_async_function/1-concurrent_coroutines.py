#!/usr/bin/env python3
"""Write an asynchronous function."""


import asyncio
from typing import Iterable
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> Iterable[float]:
    """wait and return list of time

    Args:
        n (int): number of interations
        max_delay (int): time to sleep

    Returns:
        Iterable[float]: list of time using
    """
    time_result = []
    for number in range(n):
        time_result.append(await wait_random(max_delay))
    return sorted(time_result)
