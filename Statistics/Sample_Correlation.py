from Statistics.
from .product import product
from .sum import sum # pylint: disable=redefined-builtin

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

        z_products = product(x, y)
        z_sum = sum(z_products)

        r = z_sum / (len(x) - 1)

        return(r)