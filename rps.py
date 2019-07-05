import random

options = "R", "P", "S"

user_score, computer_score, draw_score = 0, 0, 0
score_counter = {'user': user_score, 'computer': computer_score, 'draw': draw_score}


def compare(val1, val2):
    output = ""

    if val1 == "R" and val2 == "S":
        output = val1
    elif val1 == "S" and val2 == "R":
        output = val2
    elif val1 == "P" and val2 == "S":
        output = val1
    elif val1 == "S" and val2 == "P":
        output = val2
    elif val1 == "P" and val2 == "R":
        output = val1
    elif val1 == "R" and val2 == "P":
        output = val1
    elif val1 not in options:
        output = "False"
    else:
        output = "draw"

    return output

print("Welcome to RPS - The terminal adoptation of the classic Rock, Paper, Scissors game")
print("Here are the Rules:\n R = Rock, P = Paper and S = Scissors.........in case you didn't know ;) ")
print("Rock beats Scissors, Scissors beat Paper and Paper beats Rock\neither than that it's a draw")
print("Got it????\nLet's play then")

playing = True
while playing:

    game_won = False
    while not game_won:
        user_choice = input("You go 1st: Rock (R), Paper (P) or Scissors (S)? ").upper()
        computer_choice = random.choice(options)

        result = compare(user_choice, computer_choice)

        if result == user_choice:
            score_counter["user"] += 1
            print(f"You WIIINNNN!!! {user_choice} absolutely destroys {computer_choice}")
            game_won = True
        elif result == computer_choice:
            score_counter["computer"] += 1
            print(f"Computer wins!! {computer_choice} certainly destroys {user_choice}")
            game_won = True
        elif result == "False":
            print("Please insert a valid answer...if you're confused scroll up and take a look at the rules again...")
            game_won = False
        else:
            score_counter["draw"] += 1
            print(f"it was {result}\nbetter luck next time")
            game_won = True

    replay = input("Wanna play again? Y/n? ").upper()
    if replay == "Y":
        print("Restarting.....")
    elif replay == "N":
        print("Well then...goodbye\nOH...btw here is the score, if you were wondering:- ")
        print(score_counter)
        playing = False
    else:
        print("Now look what you made me do....please give a valid answer")
        playing = False
