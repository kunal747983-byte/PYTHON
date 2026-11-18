def even_reversed_odd_normal(s):
    odd = ''
    even = ''
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]
    return even[::-1] + odd  

k = 'abcde'
print(even_reversed_odd_normal(k))