import random
user_wins = 0
computer_wins = 0
options = ["snake", "water", "gun"]
# Such that 0 is snake, 1 is water and 2 is gun
while True:
    user_input = input("Type snake/water/gun to play, or q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("The computer picked" ,computer_pick + ".")
    if user_input == computer_pick:
        print("It's a tie!")
    elif user_input == "snake" and computer_pick == "water":
        print("You won!")
        user_wins += 1
    elif user_input == "water" and computer_pick == "gun":
        print("You won!")
        user_wins += 1
    elif user_input == "gun" and computer_pick == "snake":
        print("You won!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins +=1
    print("Your score is" ,user_wins)
    print("The computer's score is", computer_wins)
    if user_wins == 10 or computer_wins == 10:
        break
print(f"The total score was {user_wins} to you and {computer_wins} to the computer.")
if user_wins > computer_wins:
    print("You win!")
elif user_wins < computer_wins:
    print("The computer wins!")
else:
    print("It's a tie!")
print("Goodbye.")