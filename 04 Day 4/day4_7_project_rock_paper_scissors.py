import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose! ")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice < user_choice:
        print("You win!")
    elif computer_choice ==user_choice:
        print("It's a draw!")

""" # --- This is my program:
import random
print("Welcome to Rock, Paper, Scissors Game!")
input_user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
choices = (rock, paper, scissors)
user_choice = choices[input_user_choice]
computer_choice = random.choice(choices)

print(f"\nYou chose :\n {user_choice}")
print(f"\nComputer chose:\n {computer_choice}")

if user_choice == rock and computer_choice == rock:
    print("It's draw!")
elif user_choice == paper and computer_choice == paper:
    print("It's draw!")
elif user_choice == scissors and computer_choice == scissors:
    print("It's draw!")
elif user_choice == rock and computer_choice == scissors:
    print("You win!")
elif user_choice == paper and computer_choice == rock:
    print("You win!")
elif user_choice == scissors and computer_choice == paper:
    print("You win!")
elif user_choice == rock and computer_choice == paper:
    print("You lose!")
elif user_choice == paper and computer_choice == scissors:
    print("You lose!")
elif user_choice == scissors and computer_choice == rock:
    print("You lose!")
else:
    print("You have typed an invalid number. You lose!") """



