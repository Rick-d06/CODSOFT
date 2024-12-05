import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
while True:
  try:
    password_length = int(input("Enter the length of the password: "))
  except ValueError:
    print("Invalid input. Please enter a positive integer.")
  else:
    if password_length <= 0:
      print("Password length should be a positive integer.")
    else:
      generated_password = generate_password(password_length)
      print("Generated Password:", generated_password)
      break
