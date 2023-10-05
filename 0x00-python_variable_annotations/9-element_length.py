#!/usr/bin/env python3
'''This module contains the function for task 9'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples with the first element as the string k'''
    return [(i, len(i)) for i in lst]
