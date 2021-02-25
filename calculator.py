"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Write while loop that asks for input of numbers and the operator 
# use split function to turn the string input into a list
# Assign first item in list to operator variable, the rest to num1, num2, etc
# For each operation type, we need to write a conditional that evaluated for the operator
# calls function from arithmetic file

print("Welcome to The Calculator (part 2)")

# def check_list_length():
#     if len(equation_list) != 2
    


while True:

    user_equation = input("Enter your equation > ")

    if user_equation == "q" or user_equation == "quit":
        print("I guess I'll calc-u-later! :^)")
        break

    equation_list = user_equation.split(" ")

    operand = equation_list[0]

    num1 = equation_list[1]
    
    if len(equation_list)>2:
        num2 = equation_list[2]

    
        
    
