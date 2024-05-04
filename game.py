import random

#Global Declares
x = int

#Welcome
print('Hello, welcome to rock paper scissors')

#Input Name
name = input('What is your name' + ' ')
print("Welcome to the game" + ' ' + name)

#Random Logic
computerRange = ["rock", "paper", "scissors"]
computer = random.choice(computerRange)

#User Input
user = input("Enter a choice (rock, paper, scissors): ")
print(f"\nYou chose {user}, computer chose {computer}.\n")

#Winning Logic
x = int
if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
        x +=5
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
        x +=5
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
        x +=5
    else:
        print("Rock smashes scissors! You lose.")

#Point Logic