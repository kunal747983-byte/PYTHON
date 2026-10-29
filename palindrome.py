num = int(input())
a = str(abs(num))
if a[0:] == a[::-1] :
    print("palindrome")
else:
    print("not a palindrome")