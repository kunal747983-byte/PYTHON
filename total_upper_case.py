# def letter_digit_count(s):
#     letter_count = 0
#     digit_count = 0
#     for char in s:
#         if char.isalpha():
#             letter_count += 1
#         elif char.isdigit():
#             digit_count += 1
#     return letter_count, digit_count

# l = 'kjhfvvkjhfk12574@'
# print(letter_digit_count(l))      
    
text = 'i am learning python i love to learn python.'
# words = text.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1


# print(word_count)    

l = list(text)
letter_count = {}
for ch in l:
    if ch == ' ':
        continue
    elif ch in letter_count:
        letter_count[ch] += 1
    else:
        letter_count[ch] = 1
print(letter_count)
























