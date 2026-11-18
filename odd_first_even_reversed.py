def odd_first_even_reversed(s):
    odd = ''
    even = ''
    for i in range(len(s)):
        if i % 2 != 0:
            odd += s[i]
        else:
            even += s[i] 
    return odd + even[::-1]   

k = 'abcde'
print(odd_first_even_reversed(k))