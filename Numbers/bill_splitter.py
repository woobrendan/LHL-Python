subtotal = input("Bill total: ")
tip_percent = input("Tip Percent: ")
num_people = input("Number of people: ")

total = float(subtotal) * (1.0 + float(tip_percent) / 100)
per_person = total / float(num_people)
print(f"Each person should pay: ${per_person}")
