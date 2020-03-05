def sum(data):
    current_sum = 0

    error_compensation = 0
    corrected_current_value = 0
    next_sum = 0

    if type(data) in [int, float]:
        return (data)
    elif type(data) in [list, tuple]:
        for ii, _ in enumerate(data):
            corrected_current_value = data[ii] - error_compensation

            next_sum = current_sum + corrected_current_value

            error_compensation = next_sum - current_sum - corrected_current_value

            current_sum = next_sum

        return (round(current_sum, 3))
    else:
        raise TypeError("sum() expects an int, list, or tuple.")