player = input("Bear, Ninja, or Cowboy? > ")
print(player)

# Import the random library
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

#Generate a random role using an array
computer = roles[randint(0,2)]

while player == False:
    # Get player input
    player = input("Bear, Ninja, or Cowboy? > ")

    # Compare computer and player role

if computer == player:
    print("DRAW!")
elif computer == "Cowboy":
    if player == "Bear":
        print("You lose!", player, "is shot by", computer)
    else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
elif computer == "Bear":
    if player == "Cowboy":
        print("You win!", player, "shoots", computer)
    else: # computer is bear, player is ninja
        print("You lose!", player, "is eaten by", computer)
elif computer == "Ninja":
    if player == "Cowboy":
        print("You lose!", player, "is defeated by", computer)
    else: # computer is nninja, player is bear
        print("You win!", player, "eats", computer)                        

 player = False
computer = roles[randint(0,2)]

play_again = input("Would you like to play again? (yes/no) . ")
if play_again == 'yes':
    player = False
    computer = roles[randint(0,2)]
else:
    break    
# Make an array

# Generate a random number to pick a random element from the array