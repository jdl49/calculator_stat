from Calculator.Sum_data import sum
from Calculator.Division import division

from Statistics.Deci import decimalize

import copy


def mean(data):
    data = decimalize(copy.deepcopy(data))  # don't modify the original data
    return float(division(sum(data), len(data)))
