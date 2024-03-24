import random

welcome = input("Do you want to play?(YES/NO): ").lower()
if welcome == 'yes':
    print("Okay, let's play")
elif welcome == "no":
    print("Okay Byee!")
    quit()
else:
    print("Invalid Selection!")
    quit()

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True: 
    user_input = input("Type Rock or Paper or Scissor or Q to quit: ").lower()
    if user_input == 'q':
        print("Good Bye!")
        break
    elif user_input not in options:
        print("Please pick a valid selection")
        continue

    random_selection = random.randint(0, 2)
    computer_pick = options[random_selection]
    print("Computer picked", computer_pick + ".")
    # rock = 0, paper = 1, scissors = 2

    if user_input == "rock" and computer_pick == "scissor" :
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock" :
        print("You won!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper" :
        print("You won!")
        user_wins += 1
    else:
        print("You Lost")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")


