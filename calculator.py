# A very simple python program for a very simple calculator


numbers1 = int(input('Enter the first number: '))
operandss = input('Enter the operand: ')
numbers2 = int(input('Enter the second number: '))

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    a * b
def divide(a,b):
    a / b
if operandss == '+':
    print(add(numbers1,numbers2))
if operandss == '-':
    print(subtract(numbers1,numbers2))
if operandss == '*':
    print(multiply(numbers1,numbers2))
if operandss == '/':
    print(divide(numbers1,numbers2))