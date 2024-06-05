#TIP CALCULATOR
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are to split the bill? "))
percent = (bill * (tip / 100))
total = bill + percent
bill_per_person = total / people
final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")







