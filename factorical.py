num = int(input("Enter a number: "))
n = 1
i = 1
if num < 0 :
    print("not define")
else:
    while(num >= i):
        n = n * i
        i = i+1

    print(n)