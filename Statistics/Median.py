def median(data):
    data.sort()
    if len(data) % 2 == 1:
        return data[int(len(data) / 2)]

    middleIndex = len(data) / 2
    return (data[int(middleIndex - .5)] + data[int(middleIndex + .5)]) / 2

