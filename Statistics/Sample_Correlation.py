from Statistics.Z_score import z_scores
from Calculator.Multiplication import multiplication
from Statistics.Covariance import covariance


def correlate(x, y):
    if type(x) not in [list, tuple] or type(y) not in [list, tuple]:
        raise ValueError("To calculate correlation you need lists or tuples of "
                         "equal length. Length must be > 1.")

    if len(x) != len(y):
        raise ValueError("To calculate correlation you need lists or tuples of "
                         "equal length. Length must be > 1.")

    if len(x) <= 1 or len(y) <= 1:
        raise ValueError("Correlation requires lists of equal length where length is > 1.")

    x = z_scores(x)
    y = z_scores(y)

    z_products = multiplication(x, y)

    covar = covariance(x, y)

    r = covar / z_products

    return r
