"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator_2(string):

    tokens = string.split(" ")

    if tokens[0] == "q":
        return

    elif tokens[0] == "+":
        print(add(int(tokens[1]),int(tokens[2])))

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
        print(power(int(tokens[1]),int(tokens[2])))       

    elif tokens[0] == "mod":
        print(divide(int(tokens[1]),int(tokens[2]))) 




calculator_2("+ 2 3")
calculator_2("- 2 3")
calculator_2("* 2 3")
calculator_2("/ 2 3")
calculator_2("q")
calculator_2("mod 10 3")
calculator_2("pow 2 5")
calculator_2("cube 3")
calculator_2("square 2")