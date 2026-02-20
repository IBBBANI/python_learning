def function(data):
    n = len(data)

    for i in range(n):
        value = data[i]
        if value %2 != 0:
            data.remove(value)
    return data

print(function([1,2,3,4,5,11,14,18]))




