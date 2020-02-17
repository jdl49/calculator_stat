
def mode(data):
    dic = {}
    result = 0
    for i in data:
        if dic[i] not in dic:
            dic[i] = 0
        else:
            continue
        for copy in data:
            if i == copy:
                dic[i] +=1
    for key in dic:
        frequent = 0
        if dic[key] > frequent:
            frequent = dic[key]
            result = key

    return result


