from Statistics.Mean import mean


def variance(data, sample=True):
    if len(data) < 2:
        return None

    m = mean(data)
    if sample:  # pylint: disable=no-else-return
        return float(sum([pow(x - m, 2) for x in data]) / (len(data) - 1))
    else:
        return float(mean([pow(x - m, 2) for x in data]))
