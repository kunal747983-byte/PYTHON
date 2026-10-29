num = int(input())
n = ""
i = abs(num)
if num <= 0:
    negative_int = 0
    while i > 0:
        #negative_int = 0
        n = n + str(i % 10)
        i = i // 10
        negative_int = int(n) - 2*int(n)
    print(negative_int)
else:    

    while i > 0:
        n = n + str(i % 10)
        i = i // 10
    print(n)