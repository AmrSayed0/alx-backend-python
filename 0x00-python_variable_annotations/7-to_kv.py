#!/usr/bin/env python3
'''This module contains the function for task 7'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple with the first element as the string k'''
    return (k, float(v**2))
