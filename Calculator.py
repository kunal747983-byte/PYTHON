import sys
sys.set_int_max_str_digits(900000000)
num1 = int(input("Enter first number:"))
operator = input("Enter opertor(+, -, *, /, %, **):")
num2 = int(input("Enter second number:"))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(str((num1 / num2) * 100) + '%')
elif operator == "**":
    print(num1 ** num2)
else:
    print("invalid operator")                    

