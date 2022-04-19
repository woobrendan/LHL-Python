import math

subtotal = input("What is your subtotal? ")
tax = 0.25
total = int(subtotal) * (tax + 1)

print(f"Total tax: ${int(subtotal) * tax}")
print(f"Your total payment owed is: ${round(total, 2)} ")
