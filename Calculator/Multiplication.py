def multiplication(multiplier, multiplicant):
    if type(multiplier) not in [int, float, list, tuple] or type(multiplicant) not in [int, float, list, tuple]:
        raise TypeError('product() expects ints, floats, lists, or tuples of numbers.')

        # if you provide lists or tuples, they have to have the same length
        # for now
    if type(multiplier) in [list, tuple] and type(multiplicant) in [list, tuple] and len(multiplier) != len(multiplicant):
        raise ValueError('The two lists or tuples have to have equal lengths')

    product_vector = []

    # I'm not very happy with this if-else heavy implementation
    # but can't think of how to do this in a smarter more dynamic way

    # if both are ints, return their product
    if type(multiplier) in [int, float] and type(multiplicant) in [int, float]:
        return multiplier * multiplicant

    # if multiplier is int, multiplicant must be a float, list, or tuple
    elif type(multiplier) in [int, float]:
        for ii, _ in enumerate(multiplicant):
            product_vector.append(multiplier * multiplicant[ii])

    # if multiplicant is int, multiplier must be a float, list, or tuple
    elif type(multiplicant) in [int, float]:
        for ii, _ in enumerate(multiplier):
            product_vector.append(multiplier[ii] * multiplicant)

    # else, both are lists or tuples
    else:
        for ii, _ in enumerate(multiplier):
            product_vector.append(multiplier[ii] * multiplicant[ii])

    return product_vector
