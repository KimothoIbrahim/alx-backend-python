#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations
"""
from typing import Union, Sequence, Any, List


def safe_first_element(lst: Sequence[Any]) -> List[Union[Any, None]]:
    if lst:
        return lst[0]
    else:
        return None
