"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator_2(string):
    """Calculator program that takes a string as a parameter with the 
    operator as the prefix"""    
    

    valid = False

    while valid == False:

        string = raw_input("Enter the calculation you want to solve ")

        try:

            tokens = string.split(" ")
            operator = tokens[0]
            arguments = tokens[2:]
            running_total = int(tokens[1])

            if operator == "q":
                return

            elif operator == "+":
                for i in range(len(arguments)):
                    running_total = add(running_total, int(arguments[i]))
                print running_total

            elif operator == "-":
                for i in range(len(arguments)):
                    running_total = subtract(running_total, int(arguments[i]))
                print running_total

            elif operator == "*":
                for i in range(len(arguments)):
                    running_total = multiply(running_total, int(arguments[i]))
                print running_total

            elif operator == "/":
                for i in range(len(arguments)):
                    running_total = divide(running_total, float(arguments[i]))
                print running_total
            
            elif operator == "square":
                print square(int(tokens[1]))

            elif operator == "cube":
                print cube(int(tokens[1]))

            elif operator == "pow":
                for i in range(len(arguments)):
                    running_total = power(running_total, float(arguments[i]))
                print running_total
            
            elif operator == "mod":
                print mod(int(tokens[1]),int(tokens[2]))

            valid = True

        except:
                print "Next time, enter a real number/operator!!"
                
                instructions = open("calculator-2-instructions.txt")
                want_instructions = raw_input("Would you like instructions on how to use this program? Type yes or no ").lower()
                if want_instructions == "yes":
                    for line in instructions:
                        line = line.rstrip()
                        print line

                play_again = raw_input("Do you want to try again? Enter yes or no ").lower()
                if play_again == "yes":
                    string = raw_input("Type in another string ")




calculator_2("- 10 2 2") # 6
calculator_2("pow 2 2 2") # 16
calculator_2("/ 10 2 2") # 2.5
calculator_2("/ 10 five 2")



