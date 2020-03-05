from Statistics.Mean import mean
from Calculator.Sum_data import sum


def skew(x):
    if type(x) in [int, float]:
        return None

    mean_x = mean(x)
    n = len(x)

    m2 = sum([pow((value - mean_x), 2) for value in x]) * (1 / n)
    m3 = sum([pow((value - mean_x), 3) for value in x]) * (1 / n)

    m2_32 = pow(m2, 1.5)

    return m3 / m2_32
