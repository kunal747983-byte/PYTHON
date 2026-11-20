def make_dict_from_elems_in_index(keys, values, index: int):
    element = {}
    element[keys[index]] = values[index]
    return element

l = ['apple', 'banana', 'grapes']
p = [40, 50, 60]
i = 2 
print(make_dict_from_elems_in_index(l, p, i))