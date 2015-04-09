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
    operators = ["+","-","/","square","cube","pow","mod"]
    function_names = ["add","subtract","divide","square","cube","power","mod"]
    final_function_name = function_names[operators.index(tokens[0])]

    if tokens[0] == "q":
        return

    elif tokens[0] == "+":
        running_sum = 0
        for i in range(len(arguments)):
            running_sum = add(running_sum, int(arguments[i]))
        print running_sum

    elif tokens[0] == "-":
        print(subtract(int(tokens[1]),int(tokens[2])))

    elif tokens[0] == "*":
        print(multiply(int(tokens[1]),int(tokens[2])))    

    elif tokens[0] == "/":
        print(divide(int(tokens[1]),int(tokens[2])))
    
    elif tokens[0] == "square":
        print(square(int(tokens[1])))

    elif tokens[0] == "cube":
        print(cube(int(tokens[1])))

    elif tokens[0] == "pow":
        print(power(float(tokens[1]),float(tokens[2])))       

    elif tokens[0] == "mod":
        print(divide(int(tokens[1]),int(tokens[2]))) 




calculator_2("+ 2 3 4 5")

