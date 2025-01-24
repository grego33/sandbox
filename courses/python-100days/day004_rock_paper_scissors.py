import random

rock = "✊"
paper = "✋"
scissors = "✌️"

options = {
    0: rock,
    1: paper,
    2: scissors
}

#rock beats scissors
#paper beats rock
#scissors beats paper

player_choice = int(input("What is your choice?  Rock(0), Paper(1), Scissors(2) [0,1,2]:"))

pc_choice = random.randint(0, 2)

print(f"{options[player_choice]} vs {options[pc_choice]}")

if (player_choice == 0 and pc_choice == 2):
    print("You win!")
elif (player_choice == 1 and pc_choice == 0):
    print("You win!")
elif (player_choice == 2 and pc_choice == 1):
    print("You win!")
elif (player_choice == pc_choice):
    print("Tie...")
else:
    print("You lose :(")
