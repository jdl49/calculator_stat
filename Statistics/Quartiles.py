def get_q_value(data, p):

    q = len(data) * p

    for index, _ in enumerate(data):
        if (index + 1) >= q:
            return data[index]


def quartile(data, p=[0, .25, .5, .75, 1]):  # pylint: disable=dangerous-default-value

    # this function needs a list
    if type(data) is not list:
        raise TypeError("quantile expects a list of numerical objects.")

    data.sort()

    if type(p) in [int, float]:
        return get_q_value(data, p)
    elif type(p) is list:
        quantiles = []
        for prob in p:
            quantiles.append(get_q_value(data, prob))

        return quantiles
