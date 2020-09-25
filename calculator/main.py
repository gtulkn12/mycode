#!/usr/bin/env python3
"""Simple Calculator || Author: malik.stuckey@gmail.com"""

# Addition Function
def add(num1, num2):
    return num1 + num2

# Subtraction Function
def subtract(num1, num2):
    return num1 - num2

# Multiplication Function
def multiply(num1, num2):
    return num1 * num2

# Division Function
def divide(num1, num2):
    return num1 / num2

def calculate(operation, firstNumber, secondNumber):

    if operation == 1:
        print(firstNumber, '+', secondNumber, '=', add(firstNumber, secondNumber))
    
    elif operation == 2:
        print(firstNumber, '-', secondNumber, '=', subtract(firstNumber, secondNumber))

    elif operation == 3:
        print(firstNumber, '*', secondNumber, '=', multiply(firstNumber, secondNumber))

    elif operation == 4:
        print(firstNumber, '/', secondNumber, '=', divide(firstNumber, secondNumber))

    else:
        print('Invalid Input')

def main():

    print('Select a Operation: \n' \
        '1. Add\n' \
        '2. Subtract\n' \
        '3. Multiply\n' \
        '4. Divide\n')
    try:         
        operation = float(input('Make a selection: '))
        while operation != 1 and operation != 2 and operation != 3 and operation != 4:
            operation = float(input('Invalid operation, please enter a numeric selection: '))
        firstNumber = float(input('Enter first number: '))
        secondNumber = float(input('Enter second number: '))
    except:  
        print('Invalid Input, please enter a valid number\n')
        main()

    calculate(operation, firstNumber, secondNumber)


if __name__ == '__main__':
    main()
