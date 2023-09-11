# Don't change the code below
age = input("What is your current age?")
# Don't change the code above

# Write your code below this line
remaining_year = 90- int(age)   # 90 is expected life span year for a person
remaining_day = 365 * remaining_year
remaining_week = 52 * remaining_year
remaining_month = 12 * remaining_year


print(f"You have {remaining_day} days, {remaining_week} weeks and {remaining_month} months left.")