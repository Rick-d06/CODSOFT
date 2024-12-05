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
