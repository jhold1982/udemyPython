print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tipAsPercent = tip / 100
totalTipAmount = bill * tipAsPercent
totalBill = bill + totalTipAmount
billPerPerson = totalBill / people
finalAmount = round(billPerPerson, 2)
print(f"Each person should pay ${finalAmount}")

