"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Write while loop that asks for input of numbers and the operator 
# use split function to turn the string input into a list
# Assign first item in list to operator variable, the rest to num1, num2, etc
# For each operation type, we need to write a conditional that evaluated for the operator
# calls function from arithmetic file

print("Welcome to The Calculator (part 2)")

while True:

    user_equation = input("Enter your equation > ")

    if user_equation == "q" or user_equation == "quit":
        print("I guess I'll calc-u-later! :^)")
        break
    
    