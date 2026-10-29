# i = 1
# while i <=100:
#     print(i)
#     i += 1


# i = 100
# while i >=1:
#     print(i)
#     i -= 1
    
# n = int(input())
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1  

# n = 1
# while n <= 10:
#     print( n * n)
#     n += 1

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input())
# i = 0
# while i < len(num):
#     if (x == num[i]):
#         print("found", i)
#     # else:
#     #     print("not found")    
#     i += 1
#     # else:
#     #     print("not find")

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in num:
#     print(i)

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input())
# for i in num:
#     if x == i :
#         print("found", k)
        
# n = int(input())
# for i in range(n, n*11, n):
#     print(i)

# n = int(input())
# total = 0
# for i in range(1, n+1):
#     total += i
# print(total)

# n = int(input())
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("total sum=", sum)


# n = int(input())
# fact = 1
# i = 1
# for i in range(1, n+1):
#     fact *= i
#     i += 1
# print(fact)    
    
# def Average(a, b, c):
#     return (a + b + c)/3



# x = Average(2, 3, 6)
# print(x)

# nums = [1, 2, 5, 3, 6, 9]
# def len_list(list):
#     print(len(list))
# print(len(nums))
# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(nums)
# print()#aagar %(percentage) ke symbol aa jaye usko hatane ke liye use karte hai


# def cal_fact(n):
#     fact = 1
#     i = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(12)

# def cal_USD(n):
#     print(n*83)
#     return n*83
    
# cal_USD(5)    


# def converter(usd_val):
#     inr_val = usd_val * 95.58
#     print(usd_val, "USD =", inr_val, "INR")
# converter(int(input()))

# def checker(n):
#     if n % 2 ==0:
#         print("EVEN")
#     else:
#         print("ODD")    


# checker(int(input()))

# def sum(n):
#     if (n == 1):
#         return 1
#     else:
#         return n + sum(n-1)


# print(sum(int(input())))


# def print_list(list, idx = 0):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)


# fruit = ["mango", "litchi", "apple", "banana", ]
# print_list(fruit)

# a = int(input())
# b = int(input())
# sum = a + b
# print(sum)

# a = int(input("side of square: "))
# # b = int(input("Enter second number: "))
# Area_square = a*a
# print("Area_square =",Area_square ) 

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# sum = a + b
# Average = sum/2
# print("Average =", Average)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(a >= b)

# a = str(input("Enter your name: "))
# print(("Number of letter in your name is ="),len(a))

# str = "A single paragraph about budgeting and saving money naturally includes the $ symbol as a standard currency indicator.Planning a monthly budget requires careful tracking of every $ earned and spent to ensure long-term financial stability. When individuals set aside even a small $ amount from each paycheck into a dedicated savings account, those incremental funds accumulate significantly over time. Achieving financial goals—such as buying a home, starting a business, or building an emergency fund—depends on making smart choices about where each $ goes. By prioritizing essential expenses and cutting unnecessary costs, anyone can take control of their financial future and watch their savings grow."
# print(str.count("about"))


# a = int(input("Enter your mark: "))
# if (a >= 90):
#     print("grade = A")
# elif (90 > a >= 80):
#     print("grade = B")
# elif (80 > a >= 70):
#     print("grade = C")
# else:
#     print("grade = D")        

# n = int(input("Enter a number: "))
# if (n % 2 == 0):
#     print("EVEN")
# else:
#     print("ODD")


# A = int(input("Enter first number: "))
# B = int(input("Enter second number: "))
# C = int(input("Enter third number: "))
# if (A > B > C):
#     print("A is gerater")
# elif (B > C):
#     print("B is gerater") 
# else:
#     print("C is gerater")       

# n = int(input("Enter a number: "))
# if (n % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")    







# f = open(r"kunal.txt", "r")
# # data = f.read()
# # print(data)
# # print(type(data))
# # #f.close()
# line1 = f.readline(1)
# print(line1)

# mark = [87, 64, 33, 95, 76]
# mark.append(25)
# print(mark)
# mark.sort()
# print(mark)
# mark.sort(reverse=True)
# print(mark)
# mark.reverse()
# print(mark)
# mark.insert(3, 45)
# print(mark)
# mark.remove(95)
# print(mark)
# mark.pop(4)
# print(mark)
# mark.copy()
# print(mark)
# mark.extend([95, 65, 23, 86])
# print(mark)
# mark.clear()
# print(mark)


# print(mark[1 : 3])
# print(mark[ : 3])
# print(mark[1 : ])
# print(mark[ :: -1])

# student = ["Karan", 85, "Delhi"]
# student[0] = "Arjrn"
# print(student[0])
# print(len(student))

# tup = (87, 64, 33, 95, 33, 76, 33, 33, 45)
# print(tup[0])
# print(type(tup))
# print(tup.index(33))
# print(tup.count(33))

# class Student:
#     def __init__(self, name, mark1, mark2, mark3):
#         self.name = name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
#     # def __init__(self, name, average):

            
# s1 = Student("Karan", 80, 70, 90)
# a = s1.mark1
# b = s1.mark2
# c = s1.mark3
# sum = a + b + c
# average = sum / 3 
# print(average)       
        
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     @staticmethod
#     def hello():
#         print("hello")
            

# #     def get_avg(self):
# #         sum = 0
# #         for val in self.marks:
# #             sum += val
# #         print("hi", self.name, "your avg score is:", sum/3)

# s1 = Student("Kunal", [99, 98, 97])
# s1.hello()
# print(s1.name)
# s1.get_avg()

# s1.name = "Sumit"
# s1.get_avg()

# class Account:
#     def __init__(self, bal, acc):
#         self.bal = bal
#         self.acc = acc
#     def debit(self, debit):
#         self.bal -= debit
#         print(debit)
#         print(self.get_bal())
#     def credit(self, credit):
#             self.bal += credit
#             print(credit)
#             print(self.get_bal())  
#     def get_bal(self):
#          return self.bal          


# acc1 = Account(10000, 1234)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(4000)

# class circle:
#     def __init__(self, radius):
#         self.r = radius
        
#     #@property
#     def get_perimeter(self):
#         return float(2 * (22/7) * self.r)
    
#     #@property
#     def get_area(self):
#         return float((22/7) * self.r * self.r)

# r = circle(22)

# print(r.get_perimeter())#agar ham property ko comment out se hata diye to hamko print(get_perimeter) mese paranthesis() hatana pade ga
# print(r.get_area())#agar ham property ko comment out se hata diye to hamko print(get_area) mese paranthesis() hatana pade ga


# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
#     def showDetial(self):
#         print("role =", self.role)
#         print("department =", self.department)
#         print("salary =", self.salary)

# class Enginer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
#         super().__init__("Engineer", "IT", "75,000")       

# engg1 = Enginer("Kunal Chauhan", 20)        

# engg1.showDetial()


# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, ord2):
#         return self.price > ord2.price
    
# odr1 = Order("chip", 20)
# ord2 = Order("tea", 15)

# print(odr1 > ord2) #True


# x = int(input())
# i = 0
# while (i < x):
#     i += 1
#     print(i)

# x = int(input())
# for i in range(x):
#     print(i)

# x = int(input())
# if (x >= 0):
#     print("positive")
# else:
#     print("negative")    

# x = int(input())
# i = 0
# while (i < x):
#     i += 1
#     print(i)


# x = int(input())
# i = 1
# k = 1
# while(i <= x):
#     if (k <= x):
#         print("*" * k)
#         k += 1 
#         i += 1
    
# x = float(input())
# if (0 < x < 10):
#     print(x + 2)
# elif (10 <= x):
#     print(x**2 + 2)
# else:
#     print(0)        
    
# x = int(input())
# i = 1
# while (i <= x):
#     if (x % i == 0):
#         print(i)
#     i += 1

# x = int(input())
# print(x**2)

# T = int(input())
# if (T < 0):
#     print("INVALID")
# elif (0 <= T <= 5):
#     print("NIGHT")
# elif (6 <= T <= 11):
#     print("MORNING")
# elif (12 <= T <= 17):
#     print("AFTERNOON")
# elif (18 <= T <= 23):
#     print("EVENING")
# else:
#     print("INVALID")                

# a = int(input())
# b = int(input())
# sum = 0
# for  i in range(1000, 2000):
#     if (i % (a*b) == 0):
#         sum += i    
# print(sum)
        

# x = float(int(input("Point on x-axis = "  )))  
# y = float(int(input("Point on y-axis = "  ))) 
# if x == 0 and y == 0:
#     print("Origin")
# elif x != 0 and y == 0:
#     print("x-axis")
# elif x == 0 and y != 0:
#     print("y-axis")
# elif x > 0 and y > 0:
#     print("first quadrant")
# elif x < 0 and y > 0:
#     print("second quadrant")
# elif x < 0 and y < 0:
#     print("third quadrant")
# elif x > 0 and y < 0:
#     print("fourth quadrant")
# else:
#     print("INVALID")                    

# a = int(input("Enter the first number = " ))
# b = int(input("Enter the second number = " ))
# sum = a + b
# print("your sum = ", sum)

# n = int(input())
# i = 1
# for i in range(2, n):
#     if (n % i == 0):
#         print("np")
#         i += 1
#         break
# else:
#     print("p")    

# max_num = -1
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     elif num > max_num:
#         max_num = num
# print(max_num)


# x1 = int(input("x-coordinate of the first point = " ))
# y1 = int(input("y-coordinate of the first point = " ))
# x2 = int(input("x-coordinate of the second point = " ))
# y2 = int(input("y-coordinate of the second point = " ))
# x3 = int(input("x-coordinate of the point where you need to find y3 = " ))
# if (x2 == x1):
#     print("Vertical Line")
# else:
#     m = (y2 - y1)/(x2 - x1)    
#     if (m > 0):
#         y3 = y1 + m*(x3 - x1)
#         print(y3)
#         print("Positive Slope")
#     elif (m < 0):
#         y3 = y1 + m*(x3 - x1)
#         print(y3)
#         print("Negative Slope")
#     elif (m == 0):
#         y3 = y1 + m*(x3 - x1)
#         print(y3)
#         print("Horizontal Slope")
    

# n = int(input())
# i = 2
# for i in range(2, n):
#     if (n % i == 0):
#         i += 1
#         print("np")
#         break
#         i += 1
# else:
#     print("p")    
    
# word1 = str(input())
# word2 = str(input())
# sum = word1 + " " + word2
# print(sum)

# vechile_number = input()
# print(vechile_number[:2])

# n = int(input())
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit
#     n = n // 10
# print(sum)
    
# small_word = "1000000"
# while True:
#     n = str(input(""))
#     if (n == "abcdefghijklmnopqrstuvwxyz"):
#         break
#     elif (len(n) < len(small_word)):
#         small_word = n
# print(small_word)        


# a = bool(0)
# b = bool( )
# print(a, b)


# a = bool(-0.0)
# b = bool(0.0)
# print(a, b)

# s = str(input())
# if (len(s) % 2 == 0):
    
#     print(str[ : len(s)] + ".")

# word = input()

# # Make the length odd
# if len(word) % 2 == 0:
#     if word[-1] == '.':
#         word = word[:-1]
#     else:
#         word = word + '.'

# # Find and print the middle 3 characters
# middle = len(word) // 2
# print(word[middle - 1:middle + 2])




# word = input()

# # Step 1: Make the length odd
# if len(word) % 2 == 0:
#     if word[-1] == '.':
#         word = word[:-1]
#     else:
#         word = word + '.'

# # Step 2: Print the middle 3 characters
# mid = len(word) // 2
# print(word[mid-1:mid+2])


# n = "ha" * 3
# print(n)

# x = "Chennai"
# n = 0
# result = (x or n) or (x and n)
# print(result)

# print(True and False)
# print(True or False)
# print(not False)

# print(-13 // 4)
# print(-13 % 4)


# s = "coffee"
# print(s[1:-2])

# s = "coffee"
# print(s[10])

# s = "coffee"
# print(s[2:100])


# word = "elephant"
# print(word[::-1])

# s = "hello"
# print(s * 0)
# print(s * -2)


# value = "5"
# print(value > 3)
 
# a = "24jhagsdjhs"
# b = "jahfsrhjkedgjbe"
# print(a[:4]+"_"+b[-4:])
# a = "555"["2"]
# print(a)
# print(type(a))

# input(type('True'))
# print(10//2*5**2)
# 1value = 10
# print(1value) # 1 se start karne par error so kar rahha hai


# my-score = 95
# print(my-score)
# message = 'Use # to add a comment in Python'
# print(message)
# x, y = 2, 1
# x, y = y, x
# print(x, y)


# x = 5
# y = 6
# x = y 
# y = x
# print(x, y)
# x, y, z = 1, 3, 5
# x, y, z = y, x, z
# print(x, y, z)

# s = "underscore character"
# print("score" in s)
# print("under" in s)


# n = int(input())
# i = 0
# for i in range(0, n):
#     if (i*i == n):
#         #i += 1
#         print("prefect square")
#         break
# else:
#     print("not prefect square")    


# def Descending_Order(num):
#     digits = []
    
#     while num > 0:
#         new_num = num // 10
#         digits.append(num - new_num*10)
#         num = new_num
        
#     out = 0
#     for i, digit in enumerate(sorted(digits)):
#         out += digit * 10**i
        
#     return out

# num = 6456548675454
# print(Descending_Order(num))

# def Descending_Order(num):
#     digit = list(str(num))
#     digit.sort(reverse=True)
#     return (int(''.join(digit)))

# num = 6456548675454
# print(Descending_Order(num))


# text = """Line A
# Line B
# Line C"""
# print(text)
# path = 'C:\\Users\\Data'
# print(path)
# print("It\'s fine")
# quote = '''She said, "it's okay"'''
# print(quote)
# word = "programming"
# print(word.rfind("g"))
# print(word.rfind("z"))


# s = "nyLearning in Pythonny"
# print(s.strip('yxln'))

# word = "Data"
# print(word.startswith("d"))
# print(word.endswith("a"))
# text = "Banana Bandana"
# print(text.count("an"))
# print(text.count("Ban"))

# sentence = "I love Java and Java is fun"
# new_sentence = sentence.replace("Java", "Python", 1)
# print(new_sentence)
# word = "developer"
# print(word.index("e"))
# print(word.index("p"))
# class past:
#     def past(self, h, m, s):
#         self.h = h*3600*1000
#         self.m = m*60*1000
#         self.s = s*1000
#         return self.h + self.m + self.s
#             # Good Luck!
# h = int(input())
# m = int(input())
# s = int(input())
# obj = past()
# print(obj.past(h, m, s))
# 
# n = int(input())
# if (n%5==0):
#     print(n%10)
# else:
#     print('other')    


# import math
# print(math.pow(2, 5))
# import math
# print(math.factorial(5))
# print(math.factorial(3.5))

# from calendar import month
# print(month(2024, 6)[:14])
# print(calendar.calendar(2024))

# a = "A single quote ' and a double quote ""\""
# print(a)
# b = "A foward slash / and a backward slash ""\\"
# print(b)
# c = "Three single quotes ''' and three double quotes """"""\""""""
# print(c)
# d = "Double forward slash // and Double backward slash \\\\"
# print(d)
# import math
# def pkkk(p):
#     if (p**1/2 == int):
#         return "p" 
#     else:
#         return "np"
# p = int(input())
# print(pkkk(p))


# import math

# def pkkk(p):
#     if math.isqrt(p) ** 2 == p:
#         return "p"
#     else:
#         return "np"

# p = int(input())
# print(pkkk(p))


# def palindrominator(n):
#     if (len(n)%2 != 0):
#         return n + n[-2::-1]
#     else:
#         return n + n[::-1]

# n = input()
# #print(int(-(len(n) + 1)/2))
# print(palindrominator(n))

# def si(n, y):
#     if y < 10:
#         r = 5
#     else:
#         r = 8
#     return (n*y*r)/100        

# n = int(input())
# y = int(input())
# print(si(n, y))

# n_apples = 5
# apple_price = 5.7
# s = f"{n_apples} kgs of apple cost ₹ {n_apples*apple_price:0.2f}"
# print(s)# ans = 28.50 last me 0 must be

# n_apples = 5
# apple_price = 5.7
# s = f"{n_apples} kgs of apple cost ₹ {n_apples*apple_price:.2f}"
# print(s)# ans = 28.50 last me 0 must be

# n_apples = 5
# apple_price = 1.75
# s = f"{n_apples} kgs of apple cost ₹ {n_apples*apple_price:05.2f}"
# print(s)# ans = 08.75 first me 0 must be

# n_apples = 5
# apple_price = 1.75
# s = str(n_apples)+" kgs of apple cost ₹ 0"+str(n_apples*apple_price)
# print(s)# ans = 08.75 first me 0 must be

# s = "k"

# s = str(len(s.upper().split())).isdigit()

# print(type(s))

# s = "Kun012"
# s = s.islower()
# print(s)
# print(type(s))

# s = "Kun012"
# s = s.title()
# print(s)
# print(type(s))

# s = "Kun012"
# s = s.swapcase().title()[:5].swapcase()[:]
# print(s)
# print(type(s))

# s = "Kunh012"
# s = s.join(s.split('-'))
# print(s)
# print(type(s))

# s = "Kunh012"
# s = s.join([s[0],s[1],s[3]])
# print(s)
# print(type(s))

# f = bool(False)
# print(f)

# f = bool()
# print(f)

# a = True
# b = False
# c = True
# # if a:
# #   if b:
# #     if c:
# #       print('c')
# #     print('b')
# #   print('a')

# # if a:
# #   if b:
# #     if c:
# #       print('c')
# #     else:
# #       print('b')
# #   else:
# #     print('a')


# if a:
#   if b:
#       print('ab')
#   if c:
#       print('ac')

# if not (not a or not b):
#     print('ab')
# if not (not a or not c):
#     print('ac')

# from math import pi as math_pi

# s = "abcdefghijklmnopqrstuvwxyz"
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# print(s[-a:-len(s):-3])
# print(s[::-b])
# print(s[c:0:-3])
# print(s[len(s):-d:-3])
# print(s[:e:-3])


# dept    = input()
# course  = input()
# prefix  = input()
# name    = input()
# roll_no = input()
# name = prefix + " " + name.upper() # one space
# lib_id = dept[0] + course[0] + roll_no
# print("Student record:")
# indent = '    '	# four spaces
# print(indent + "Dept:", dept)
# print(indent + "Name:", name)
# print(indent + "Roll No:", roll_no)
# print(indent + "Library Card No:", lib_id)


# L is a positive integer that has already been defined at this stage
# L = 5
# word = input()
# space = ' ' # there is a single space
# if len(word) < L:
#     word = 'short' + ' ' + word
# elif L <= len(word) < 2 * L:
#     word = 'medium' + ' ' + word
# else:
#     word = 'long' + ' ' + word
# print(word)

# a = False
# b = False
# c = True

# # if a:
# #   if b:
# #       print('OK')
# #   if c:
# #       print('OK')

# if a and b or c:
#     print('OK')


# a = int(input())
# b = int(input())
# if a > 0:
#     if b < 0:
#         print('OK')


# if int(input()) > 0 and int(input()) < 0:
#     print('OK')

# x = 5
# while x > 0:
#     print(x)
# x = 0
# while x < 5:
#     x = x + 1
# print(x)

# x = 10
# while x < 5:
#     print("Hello")
#     x = x - 1
# print("Done")

# x = 1
# while x != 10:
#     print(x)
#     x = x + 2

# count = 0
# while count < 3:
#     print("Attempt", count)
#     count = count + 1
#     if count == 2:
#         count = 0
# n = 0
# while n >= 0:
#     n = n+1

# n = int(input())
# i = 1
# while n >= 1:
#     print (i * i)
#     i += 1

# n = int(input())
# total = 0
# while n!=0:
#     total+=n
#     n = int(input())
# print(total)


# total = 0
# while True:
#     n = int(input())
#     if n==0:
#         break
#     total+=n
# print(total)

# n = int(input())
# answer = 1
# i = 1
# while i <= n:
#     answer = answer * i
#     i = i + 1
# print(answer)

# n = 5
# answer = 1
# i = 1
# while i <= n:
#     i = i + 1
#     answer = answer * i
# print(answer)


# n = 3
# answer = 1
# i = 1
# while i < n:
#     answer = answer * i
#     i = i + 1
# print(answer)

# n = 5
# answer = 1
# i = 1
# while i <= n:
#     answer = answer * i
#     if answer > 1000:
#         i = i + 1
# print(answer)

# n = 5
# answer = 1
# i = 1
# while i <= n:
#     answer = answer + i
#     i = i + 1
# print(answer)


# n = 5.00
# answer = 1
# i = 1
# while i <= n:
#     answer = answer * i
#     i = i + 1
# print(answer)

# n = int(input())
# fac = 1
# i = 1
# if n < 0:
#     print ("Not Define")
# else:    
#     while i <= n:
#         fac = fac * i
#         i += 1
#     print(fac)
        

# n = int(input())
# if n < 0:
#     r = str(n)
#     k = r.lstrip('-')
#     print(len(k))
# else:
#     print(len(str(n)))    

# n = int(input())
# if n < 0:
#     r = abs(n)
#     k = str(r)
#     print("-" + k[::-1])
# else:
#     r = str(n)
#     print(r[::-1])
    
# n = abs(int(input()))
# k = str(n)

# num = int(input("Enter the number: "))
# factorial = 1
# while num > 0:
#     factorial = factorial * num
#     num = num - 1
# print(factorial)

# num = abs(int(input("Enter a number: ")))
# digits = 1
# while num > 9:
#     num = num // 10
#     digits = digits + 1
# print(digits)


# num = 205
# digits = 1
# while num > 9:
#     num = num // 10
#     digits = digits + 1
# print(digits)


# num = int(input("Enter a number: "))
# reverse = 0
# while num > 0:
#     r = num % 10
#     num = num // 10
#     reverse = reverse * 10 + r
# print(reverse)

# reverse = 4321
# negated = reverse - 2 * reverse
# print(negated)

# for i in range(5):
#     print(i)

# count = 0
# for i in range(5):
#     if i % 2 == 0:
#         count = count + 1
# print(count)

# for i in range(3):
#     i = i + 10
#     print(i)

# for i in range(3):
#     print(i)

# ans = 0
# for i in range(3):
#     ans = ans + i * i
# print(ans)

# prod = 0
# for i in range(1, 5):
#     prod = prod * i
# print(prod)

# ans = 0
# for i in range(10):
#     if i % 3 == 0:
#         ans = ans + i
# print(ans)

# result = ""
# for i in range(3):
#     result = result + str(i)
# print(result)

# ans = 0
# for i in range(6):
#     ans = ans + i
# print(ans)

# for i in range(7, 7):
#     print(i)

# for i in range(10, 5):
#     print(i)

# count = 0
# for ch in "Python":
#     if ch in "aeiouAEIOU":
#         count = count + 1
# print(count)

# result = ""
# for ch in "Hi":
#     result = ch + result
# print(result)

# for i in range(1, 10, -1):
#     print(i)

#print(f"[{5:<5d}]")
#print(f"[{123:<5d}]")

#print(f"[{5:>5d}]")
# print(f"[{5:05d}]")
# print(f"[{42:05d}]")
#print(f"[{5:*^5d}]")
# pi = 3.14159
# print(f"[{pi:8.2f}]")
#print("Total:", 100, sep="", end="!\n")

# values = "7,3,9,-1"
# nums = values.split(",")
# i = 0
# count = 0
# total = 0
# while int(nums[i]) != -1:
#     total = total + int(nums[i])
#     count = count + 1
#     i = i + 1
# print(count, total)

# str_num = "5847"
# reverse = ""
# for c in str_num:
#     reverse = c + reverse
# print(reverse)

#print("Zebra" < "apple")

# number = 1221
# str_num = str(abs(number))
# reverse = ""
# for c in str_num:
#     reverse = c + reverse
# if number < 0:
#     reverse = "-" + reverse
# print(number == reverse)

# num = 6
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


# n = 17
# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break
# print(is_prime)

# word = "PYTHON"
# print(word[6])

# for i in range(3):
#     for j in range(3):
#         print(i, j)

# count = 0
# for i in range(6):
#     for j in range(3):
#         count = count + 1
# print(count)

# count = 0
# for i in range(4):
#     for j in range(i):
#         count = count + 1
# print(count)

# for i in range(4):
#     for j in range(4):
#         if i + j == 4:
#             print(i, j)

# total = 0
# for i in range(1, 4):
#     for j in range(1, 4):
#         total = total + (i * j)
# print(total)

# i = 15
# flag = True
# for j in range(2, i):
#     if i % j == 0:
#         flag = False
#         break
# print(flag, j)

# total_inner = 0
# for i in range(2, 7):
#     flag = True
#     for j in range(2, i):
#         total_inner = total_inner + 1
#         if i % j == 0:
#             flag = False
#             break
# print(total_inner)

# emp = input()
# while emp != "-1":
#     profit_loss = 0
#     trade = int(input())
#     while trade != 0:
#         profit_loss = profit_loss + trade
#         trade = int(input())
#     print(emp, profit_loss)
#     emp = input()

# days = int(input())
# for day in range(1, days + 1):
#     total = 0
#     val = int(input())
#     while val != -1:
#         total = total + val
#         val = int(input())
#     print(day, total)

# max_length = 0
# word = input()
# while word != "-1":
#     count = 0
#     for letter in word:
#         count = count + 1
#     if count > max_length:
#         max_length = count
#     word = input()
# print(max_length)

# count = 0
# for i in range(5):
#     if i % 2 == 0:
#         pass
#     else:
#         count = count + 1
# print(count)

# count = 0
# n = 0
# while n < 5:
#     n = n + 1
#     if n == 3:
#         continue
#     count = count + 1
# print(count, n)

# total = 0
# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     if i > 7:
#         break
#     total = total + i
# print(total)

# total = 0
# found = False
# for i in range(1, 5):
#     if found:
#         break
#     for j in range(1, 5):
#         if j % 2 == 0:
#             continue
#         total = total + (i * j)
#         if total > 15:
#             found = True
#             break
# print(total)

# count = 0
# for i in range(3):
#     for j in range(3):
#         if j == 1:
#             break
#         count = count + 1
# print(count)

# n = int(input())
# i = 1
# while (i <= n):
#     if (n % i == 0):
#         print(i)
#     i = i + 1

# x = 1
# while (x*2 + x + 41) % 41 != 0:
#     x = x + 1
# print(x)

# i = 0
# while (i < 1000000000000000000):
#     print(i * '*')
#     i = i + 1

# y = {10, 20, 30}
# z = list(y)
# print(z[0])
# print(y[0])

# z = {"Amit", "Neeru", "Anamika"}
# z.append('kunal')
# print(z)


# import sys

# a = list(range(5))
# t = tuple(range(5))
# print(a == list(t))
# print(sys.getsizeof(a) > sys.getsizeof(t))

# t = (2, 7, 18, 64)
# print(t)
# print(t[0])

# alpha = tuple("abcde")
# r = []
# for ch in "cabbage123":
#     if ch in alpha:
#         r.append(ch)
# print("".join(r))

# s = set()
# s.add(1)
# s.add(1)
# s.add((1, 2))
# s.add((1, 2))
# print(len(s))


# t = (1,2,5, 4,3)
# # print(t[0:2])
# # print(t[1])
# l = list(t)
# l.reverse()
# j = tuple(l)
# print(j)
# print(t[::-1])




































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































