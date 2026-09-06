#Python Project 2: Generate a random password

import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special = "[]{()}!@#$%^&*<>?/|"

length = int(input("Enter the length of the password: "))

allCharacters = upper + lower + numbers + special

password = "".join(random.sample(allCharacters, length))

print("Generated Password:", password)