#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a
new function task_wait_n.
The code is nearly identical to wait_n
except task_wait_random is being called.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    args: n - int
          max_delay - int
    Returns: list[float]
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    lst = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        inserted = False
        for i in range(len(lst)):
            if delay < lst[i]:
                lst.insert(i, delay)
                inserted = True
                break
        if not inserted:
            lst.append(delay)
    return lst
