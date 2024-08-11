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
user = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
"""
rock 0  beats scisssor 2
scissor 2 beats paper 1
paper 1 beats rock 0
"""
ai = random.randint(0, 2)
asci = [rock, paper, scissors]

if user == 0 or user == 1 or user == 2:
    print(asci[user])
    print(f"Computer choose:\n {asci[ai]}")
    """
# progam logic
    if user == ai:
        print("Its a Draw")
    elif user == 0:  # rock
        if ai == 1:  # paper
            print("You lose")
        else:  # user = rock and ai = scissors
            print("You win")
    elif user == 1:  # paper
        if ai == 2:  # scissors
            print("You lose")
        else:  # paper rock
            print("You win")
    elif user == 2:
        if ai == 0:
            print("You lose")
        else:
            print("You win")
    """
# alternate logic
    """
    if user == ai:
        print("Its a Draw")
    elif user == 0 and ai == 2:
        print("You win")
    elif user == 2 and ai == 0:
        print("You lose")
    elif user > ai:
        print("You win")
    else:
        print("You lose")
    """

# alternate
    if user == ai:
        print("Its a Draw")
    elif (
            (user == 0 and ai == 2) or
            (user == 1 and ai == 0) or
            (user == 2 and ai == 1)
    ):
        print("You win")
    else:
        print("You lose")
else:
    print("You have typed an invald number")
