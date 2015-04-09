"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator_2(string):

    tokens = string.split(" ")
    arguments = tokens[1:]

    if tokens[0] == "q":
        return

    elif tokens[0] == "+":
        running_total = 0
        for i in range(len(arguments)):
            running_total = add(running_total, int(arguments[i]))
        print running_total

    elif tokens[0] == "-":
        running_total = 0
        for i in range(len(arguments)):
            running_total = subtract(running_total, int(arguments[i]))
        print running_total

    elif tokens[0] == "*":
        running_total = 0
        for i in range(len(arguments)):
            running_total = multiply(running_total, int(arguments[i]))
        print running_total

    elif tokens[0] == "/":
        running_total = 0
        for i in range(len(arguments)):
            running_total = divide(running_total, int(arguments[i]))
        print running_total
    
    elif tokens[0] == "square":
        print(square(int(tokens[1])))

    elif tokens[0] == "cube":
        print(cube(int(tokens[1])))

    elif tokens[0] == "pow":
        running_total = 0
        for i in range(len(arguments)):
            running_total = power(running_total, int(arguments[i]))
        print running_total      

    elif tokens[0] == "mod":
        print(divide(int(tokens[1]),int(tokens[2]))) 




calculator_2("pow 2 2 2")

