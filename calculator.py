# -*- coding: utf-8 -*-
"""Calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iQfBzIx7t0FawxkUS0rI0PM3TSVmrsyG
"""

while True:
  try:
    num1 = int(input("Enter first number: "))
    break
  except ValueError:
    print("Invalid input. Please enter a number.")
while True:
  try:
    num2 = int(input("Enter second number: "))
    break
  except ValueError:
    print("Invalid input. Please enter a number.")
opperation = input("Enter operation: ")
if opperation == "+":
    print(f"Result is: {num1 + num2}")
elif opperation == "-":
    print(f"Result is: {num1 - num2}")
elif opperation == "*":
    print(f"Result is: {num1 * num2}")
elif opperation == "/":
    print(f"Result is: {num1 / num2}")
else:
    print("invalid operation")