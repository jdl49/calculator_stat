from Statistics.Variance import variance
from Calculator.SquareRoot import squareRoot


def standard_deviation(data, sample=True):
    return squareRoot(variance(data, sample))
# square of variance
