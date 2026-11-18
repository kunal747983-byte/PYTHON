def alternate_case(s):
    E = ''
    for i in range(len(s)):
        if i % 2 == 0:
            E += s[i].upper()
        else:
            E += s[i]    
    return E        


k = 'abcde'
print(alternate_case(k))