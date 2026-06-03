#Introduction
print("Welcome to the tip caluculator!")

#User inputs total bill amount
total = float(input("what was the total amount? $"))

#User inputs desired tip amount percentage
tip = int(input("what is the tip amount? 10, 12, 15: "))

#User inputs the number of people splitting the bill
people = int(input("how many people are spliting ? "))

#The amount of the bill is calculated, including the tip
bill_with_tip = tip/100 * total + total

#Final statement is printed with the total bill amount divided by the number of people. The ':.2f'is there to show only up to the 2nd decimal point.
print (f"Each person should pay: ${bill_with_tip / people:.2f}")
