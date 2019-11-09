#!/usr/local/bin/python3

from collections import OrderedDict

print("# my_first_calculator.py")
print("# TODO: make it work for floating point numbers too")
print("")
print("if 3/2 == 1: # because python 2 does not know maths")
print("    input = raw_input # python 2 compatibility")
print("")
print('welcome to this calculator')
print('it can add, subtract, and multiply whole numbers')
print("num1 = int(input('enter first number: '))")
print("sign = input('what operation do you want to do? +, -, /, or *: ')")
print("num2 = int(input('enter second number: '))")
print("")

signs = ["+", "-", "/", "*"]

for i in range(50):
    for sign in signs:
        for j in range(50):
            try:
                output = eval(f"{i}{sign}{j}")
                print(f"if num1 == {i} and sign == '{sign}' and num2 == {j}:")
                print(f'     print()"{i}"{sign}{j} = {output}")')
            except ZeroDivisionError:
                pass