# Imports
import sys # Import the sys module
import random # Import the random module
from enum import Enum # Import the Enum class from the enum module

# Enum class
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
# # Print the Enum class
# print(RPS(2))
# print(RPS(2).name)
# print(RPS(2).value)
# print(RPS['ROCK'])
# sys.exit()

print("") # This is a blank line to separate games

# Rock, Paper, Scissors
playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

# Casting the input to an integer
player = int(playerchoice)

# If statements
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3") # Exit the program if the user enters an invalid number
      
computerchoice = random.choice("123") # Randomly select a number between 1 and 3
computer = int(computerchoice) # Cast the number to an integer

print("")
print("You choose " + str(RPS(player).name) + ".")
print("The computer chooses " + str(RPS(computer).name) + ".")
print("")

if player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You win!")
elif player == computer:
    print("It's a tie!")
else:
    print("You lose!")