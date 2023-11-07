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
choice_list = [rock, paper, scissors]
p1_choice = int(input("What do you choose? Type:\n 0 for Rock,\n 1 for Paper, \n 2 for Scissors\nYour Answer:"))
p2_choice = random.randint(0, 2)

if p1_choice >= 3 or p1_choice < 0:
    print("You Broke The game rules you lose!")
else:
    player1 = choice_list[p1_choice]
    player2 = choice_list[p2_choice]

    print("Player 1:")
    print(player1)
    print("Player 2:")
    print(player2)

    if p1_choice == 0 and p2_choice == 2:
        print("You win")
    elif p1_choice == 2 and p2_choice == 0:
        print("You Lose")
    # todo scissors lose rock
    elif p1_choice < p2_choice:
        print("You Lose")
    # todo rock win scissors
    elif p1_choice > p2_choice:
        print("You win")
    elif p1_choice == p2_choice:
        print("Draw")
    else:
        print("You Lose")
