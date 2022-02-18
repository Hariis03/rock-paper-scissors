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


player = int(input("What do you wanna choose?\n1-Rock\n2-Paper\n3-Scissors\n"))

if player == 1:
  print(rock)
elif player == 2:
  print(paper)
elif player == 3:
  print(scissors)
else:
  print("Please enter a valid command!")

pc = random.randint(1, 3)
print(f"Computer chose:")

if pc == 1:
  print(rock)
elif pc == 2:
  print(paper)
else:
  print(scissors)

# Game Logic
  
# Rock if statement
if player == 1 and pc == 1:
  print("It's a tie!")
elif player == 1 and pc == 2:
  print("You Lose!")
elif player == 1 and pc == 3:
  print("You Win!")

  
#Paper if statement     
if player == 2 and pc == 1:
  print("You Win!")
elif player == 2 and pc == 2: 
  print("It's a tie!")
elif player == 2 and pc == 3:
  print("You Lose!")
   
#Scissors if statement
if player == 3 and pc == 1:
  print("You Lose!")
elif player == 3 and pc == 2:
  print("You Win!")
elif player == 3 and pc == 3:
  print("It's a tie!")

  
