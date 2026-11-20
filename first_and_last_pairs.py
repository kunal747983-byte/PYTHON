def first_and_last_pairs(keys, values):
    element = {}
    element[keys[0]] = values[0]
    element[keys[-1]] = values[-1]
    return element
l = ['apple', 'banana', 'grapes']
p = [40, 50, 60]
print(first_and_last_pairs(l, p))



























