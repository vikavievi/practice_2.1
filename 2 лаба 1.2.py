def sum_dct(*dicts):
    result = {}
    for i in dicts:
        for key, cifra in i.items():
            if key in result:
                result[key] += cifra
            else:
                result[key] = cifra
    return result

dict1 = {"a": 5, "b": 10, "c": 15}
dict2 = {"a": 5, "b": 3, "c": 7}
dict3 = {"t": 2, "b": 8, "v": 12}

result = sum_dct(dict1, dict2, dict3)
print('Результат вывода', result)
