def interleave(s, k):
    E = ''
    if len(s) < len(k) or len(k) < len(s):
        l = s[len(k): ] or k[len(s): ]
        
    for i in range(len(s)):
        for j in range(len(k)):
                if i == j:
                    E += s[i] + k[j]
                    o = E + l
            
                
              
            
    return o        
    
m = 'abc'
n = 'xyz12'
print(interleave(m, n))