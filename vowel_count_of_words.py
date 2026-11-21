
snt = input()
k = snt.split()
output = ''
def vowel_count(s):
    count = 0
    vowel = 'AEIOUaeiou'

    for i in s:
        if i in vowel:
            count += 1
    return count
for i in k:
    output += i + "(" + str(vowel_count(i)) + ") "
print(output)
   












































































