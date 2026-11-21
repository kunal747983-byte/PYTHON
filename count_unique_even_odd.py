def count_unique_even_odd(l:list)->dict:
    element = {}
    k = set(l)
    even_count = 0
    odd_count = 0
    for i in k:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    element["even"] = even_count
    element["odd"] = odd_count
    return element
l = [1, 2, 3, 2, 4, 4, 3, 6]
print(count_unique_even_odd(l))
