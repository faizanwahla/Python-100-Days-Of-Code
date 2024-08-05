print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(
    input("How much tip would you like to give? 10, 12, or 15?"))

people = int(input("How many people to split the bill?"))

tip = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + tip
bill_per_person = (total_bill_with_tip / people)

# bill_per_person = round((total_bill_with_tip / people), 2)

bill_per_person = "{: .2f}".format(bill_per_person)
print(f"Each person should pay: ${bill_per_person}")
