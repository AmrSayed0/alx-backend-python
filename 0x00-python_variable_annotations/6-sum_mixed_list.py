#!/usr/bin/env python3
'''This module contains the function for task 6'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Sums a list of floats and returns their sum as a float.'''
    return float(sum(mxd_lst))
