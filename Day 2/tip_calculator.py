print()
print()
print()
print("----------------Welcome to tip Calculator----------------")
bill = float(input("What was the total bill: "))
tip_percent = float(input("How much tip do you want to give: "))/100
people = int(input("How many people are there to divide bill into: "))

total_bill = (bill * (tip_percent) + bill)
print(f"Your total bill is: {total_bill/people}")

