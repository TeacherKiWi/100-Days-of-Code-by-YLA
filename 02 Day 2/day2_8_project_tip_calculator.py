# Tip Calculator
print("Welcome to the tip calculator...")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = round((total_bill) * (tip_percentage/100),2)
# print(f"Tip is {tip}")
# print(f"Total bill is {total_bill}")
people = int(input("How many people to split the bill? "))
final_bill = total_bill + tip
bill_per_person = final_bill/people
print(f"Each person should pay: ${bill_per_person}")
