#!/usr/bin/env python3
"""
write an async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    args: n - int
          max_delay - int
    Returns: list[float]
    """
    lst = []
    for i in range(n):
        delay = await wait_random(max_delay)
        inserted = False
        for i in range(len(lst)):
            if delay < lst[i]:
                lst.insert(i, delay)
                inserted = True
                break
        if not inserted:
            lst.append(delay)
    return lst
