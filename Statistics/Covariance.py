from Statistics.Mean import mean


def covariance(x, y):
    if type(x) not in [list, tuple] or type(y) not in [list, tuple]:
        raise ValueError("To calculate covariance you need lists or tuples of "
                         "equal length. Length must be > 1.")

    if len(x) != len(y):
        raise ValueError("To calculate covariance you need lists or tuples of "
                         "equal length. Length must be > 1.")

    if len(x) <= 1 or len(y) <= 1:
        raise ValueError("covariance requires lists of equal length where length is > 1.")

    xmean = mean(x[:])
    ymean = mean(y[:])

    covsum = 0
    n = len(x)

    for ii in list(range(n)):
        covsum += (x[ii] - xmean) * (y[ii] - ymean)
        
    bessels_correction = n - 1

    return covsum / bessels_correction
