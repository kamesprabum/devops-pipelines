print("Welcome to game ")
print("number shoud be between 1 to 50")
User_input =input("Press Enter to start the game...")

import random
secret_number = random.randint(1, 50)

for i in range(10):
 try:

    User_input = int (input("enter your guess: "))
    if User_input < 1 or User_input > 50:
        print("Error: The secret number must be between 1 and 50.")

    if User_input < secret_number:
        print("Your guess is too low. Try again.")
    elif User_input > secret_number:
        print("Your guess is too high. Try again.")

    

    
    if User_input == secret_number:
    
        print("Congratulations! You guessed the correct number.")
        break
 except ValueError:
    print("hey idiot, play the game, not play with game")
else:
        print ("ur trail is over man pay now :) lol")


