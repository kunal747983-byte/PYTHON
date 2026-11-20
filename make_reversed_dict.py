def make_reversed_dict(keys, values, index: int):
    element = {}
    element[values[index]] = keys[index]
    return element
keys = ['apple', 'banana', 'cherry']
values = [10, 20, 30, 40]
i = 2
print(make_reversed_dict(keys, values, i))