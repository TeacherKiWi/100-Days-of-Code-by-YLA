import random
# Split string method
# --- convert string to a list --> https://www.askpython.com/python/string/convert-string-to-list-in-python
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# --- get the total numbers of item in the list
num_items = len(names)
# print(num_items)
# --- generate random choice from 0 to last item in the list
random_item = random.randint(0, num_items-1)
# print(random_item)
random_names = names[random_item]
print(random_names + " is going to buy the meal today!")


# --- another method using random module
# --- random.choice()-->https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
# random_names1 = random.choice(names)
# print(random_names1 + " is going to buy coffee today!")
