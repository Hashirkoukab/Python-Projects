#Addition
def add(num1, num2):
    return num1 + num2
#Subtraction
def subtract(num1, num2):
    return num1 - num2
#Multiply
def multiply(num1, num2):
    return num1 * num2
#Divide
def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2
select = int(input("Select operation from 1 = Add, 2 = Subtract, 3 = Multiply, 4 = Divide:"))

number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))