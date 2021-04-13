
import random

comp_choice = ['Rock', 'Paper', 'Scissors']

print('''\nThis is a ROCK, PAPER, SCISSORS game
You will compete against computer which will randomly generate rock, paper or scissors
Whoever scores 3 points first will win the match''')

user_name = input("\nEnter your name: ")
print(f"Welcome {user_name}!")

comp_points = 0
user_points = 0

def outcomes():
    result1 = "User Wins!"
    result2 = "Computer Wins!"
    result3 = "TIE!"
    if(comp_move == 'Rock' and user_move == '1'):
        return result3
    elif(comp_move == 'Rock' and user_move == '2'):
        return result1
    elif(comp_move == 'Rock' and user_move == '3'):
        return result2
    elif(comp_move == 'Paper' and user_move == '1'):
        return result2
    elif(comp_move == 'Paper' and user_move == '2'):
        return result3
    elif(comp_move == 'Paper' and user_move == '3'):
        return result1
    elif(comp_move == 'Scissors' and user_move == '1'):
        return result1
    elif(comp_move == 'Scissors' and user_move == '2'):
        return result2
    elif(comp_move == 'Scissors' and user_move == '3'):
        return result3

user_move = 0

while True:
    comp_move = random.choice(comp_choice)

    user_move = input('''\nWhat do you want to choose?
Press 1 for Rock
Press 2 for Paper
Press 3 for Scissors\n''')
    if(user_move == '1'):
            print(f'''\n{user_name} has chosen Rock and computer has chosen {comp_move}
Doing Rock v/s {comp_move} and....''')
            print(outcomes())
            if(outcomes() == "User Wins!"):
                user_points += 1
                print("\nUser points:",user_points)
                print("Computer points:", comp_points)
            elif(outcomes() == "Computer Wins!"):
                comp_points += 1
                print("\nUser points:", user_points)
                print("Computer points:",comp_points)
            else:
                print("\nUser points:", user_points)
                print("Computer points:", comp_points)


    elif (user_move == '2'):
            print(f'''\n{user_name} has chosen Paper and computer has chosen {comp_move}
Doing Paper v/s {comp_move} and....''')
            print(outcomes())
            if (outcomes() == "User Wins!"):
                user_points += 1
                print("\nUser points:", user_points)
                print("Computer points:", comp_points)
            elif (outcomes() == "Computer Wins!"):
                comp_points += 1
                print("\nUser points:", user_points)
                print("Computer points:", comp_points)
            else:
                print("\nUser points:", user_points)
                print("Computer points:", comp_points)


    elif (user_move == '3'):
            print(f'''\n{user_name} has chosen Scissors and computer has chosen {comp_move}
Doing Scissors v/s {comp_move} and....''')
            print(outcomes())
            if (outcomes() == "User Wins!"):
                user_points += 1
                print("\nUser points:", user_points)
                print("Computer points:", comp_points)
            elif (outcomes() == "Computer Wins!"):
                comp_points += 1
                print("\nUser points:", user_points)
                print("Computer points:", comp_points)
            else:
                print("\nUser points:", user_points)
                print("Computer points:", comp_points)
    elif(user_move == ''):
        print("Please enter something!")

    else:
        print("Please enter a valid choice!")

    if(user_points == 3):
            print(f"{user_name} wins this round!")
            break
    elif(comp_points == 3):
            print("Computer wins this round")
            break
