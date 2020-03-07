def mode(data):
    dic = {}
    result = 0
    frequent = 0
    for i in data:
        if i not in dic:
            dic[i] = 0
        else:
            continue
        for copy in data:
            if i == copy:
                dic[i] += 1
    for key in dic:
        if dic[key] > frequent:
            frequent = dic[key]
            result = key

    return result
