#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations
"""
from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None
