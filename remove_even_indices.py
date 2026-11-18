def remove_even_indices(s):
    odd = ''
    for ch in range(len(s)):
        if ch % 2 != 0:
            odd += s[ch]
    return odd        

t = 'abcdef'
print(remove_even_indices(t))