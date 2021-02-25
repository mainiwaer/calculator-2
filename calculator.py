"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Write while loop that asks for input of numbers and the operator 
# use split function to turn the string input into a list
# Assign first item in list to operator variable, the rest to num1, num2, etc
# For each operation type, we need to write a conditional that evaluated for the operator
# calls function from arithmetic file


# Make function that processes input and makes sure it is valid before following through
    # 






print("Welcome to The Calculator (part 2)")

# def check_list_length():
#     if len(equation_list) != 2

def check_input():
    while True:
        user_equation_input = input("Enter your equation > ")
        
        equation_list = user_equation_input.split(" ")

        valid_input_list = ["+", "-", "*", "/", "square", "cube", "pow", "mod", "q"]
        number_indexes = [1, 2]

        if "q" in equation_list:
            return ["q"]

        if equation_list[0] not in valid_input_list: 
            print(equation_list[0])
            print("That is not a valid operation, try again.")
        
        for number in number_indexes:
            print(number)
            if equation_list[number].isnumeric() != True:
                print("Please use numbers in the equation.")            

        else:
            return equation_list

    


while True:

    equation_list = check_input()

    if "q" in equation_list:
        print("I guess I'll calc-u-later! :^)")
        break

    operand = equation_list[0]

    num1 = float(equation_list[1])

    if len(equation_list)>2:
        num2 = float(equation_list[2])

    if operand == '+':
        print(add(num1, num2))

    if operand == '-':
        print(subtract(num1, num2))
    
    if operand == '*':
        print(multiply(num1, num2))
    
    if operand == '/':
        print(divide(num1, num2))

    if operand == 'square':
        print(square(num1))

    if operand == 'cube':
        print(cube(num1))

    if operand == 'pow':
        print(power(num1, num2))

    if operand == 'mod':
        print(mod(num1, num2))
    
