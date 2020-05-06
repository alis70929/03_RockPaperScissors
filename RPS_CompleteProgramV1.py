# Rock paper scissors complete program version 1
# Is only a rough putting together of all the components as i go, a more polished version will be made at the end.

# Imports go here
import random


# Functions go here
def int_checker(question,low):
    while True:
        try:
            response = int(input(question))
            if response <= low:
                print("Please enter a whole number above 0")
                continue
            return response
        except ValueError:
            print("Please enter a whole number above 0")


# Main code
# Counts how many rounds user has won lost or drawn
winlosscounter = []
# loops until user gives a valid answer for game mode
game_mode_valid = False
while not game_mode_valid:
    # Ask user which game mode they would like to play
    game_mode = input("Normal(N) or Variant(V)?").lower()

    # Give user confirmation on which game mode they have chosen
    if game_mode == "n" or game_mode == "normal":
        print("You have chosen normal rules for rock paper scissors")
        game_mode_valid = True
    elif game_mode == "v" or game_mode == "variant":
        print("You have chosen variant rules for rock paper scissors lizard spock")
        game_mode_valid = True
    # If user inputs anything other than the given choices print an error message
    else:
        print("Please choose either Normal(N) or Variant(V) rules")

# Loops till we get a valid answer for rounds
rounds_valid = False
while not rounds_valid:
    # ask how many rounds they would like to play and check if it an int
    rounds = int_checker("Best out of ?:", 1)
    # check if rounds is an odd number to avoid overall draws
    if rounds % 2 == 0:
        # error message if rounds is even
        print("Please enter an odd number above 0")
        continue
    rounds_valid = True

# Loops until user gives a valid answer for attack choice
game_outcome = 0
attack_choice_valid = False
while not attack_choice_valid:
    # Depending on which game mode user chooses alter the question
    if game_mode == "n" or game_mode == "normal":
        attack_choice = input("Please chose from Rock(R), Paper(P) or Scissors(S)").lower()
    elif game_mode == "v" or game_mode == "variant":
        attack_choice = input("Please chose from Rock(R), Paper(P), Scissors(S), Lizard(L) or Spock(Sp)").lower()

    # Assign chosen attack with an icon and numerical value
    if attack_choice == "r" or attack_choice == "rock":
        chosen_attack_icon = "🥔"
        game_outcome += 3
    elif attack_choice == "p" or attack_choice == "paper":
        chosen_attack_icon = "📰"
        game_outcome += 2
    elif attack_choice == "s" or attack_choice == "scissors":
        chosen_attack_icon = "✂"
        game_outcome += 1
    elif game_mode == "v" or game_mode == "variant":
        if attack_choice == "l" or attack_choice == "lizard":
            chosen_attack_icon = "🦎"
            game_outcome += 4
        elif attack_choice == "sp" or attack_choice == "spock":
            chosen_attack_icon = "🖖"
            game_outcome += 5
    # If user inputs something that is not one of the above then loop question again
    else:
        continue
    # once we are given a valid answer the loop ends
    attack_choice_valid = True

# Alters the computers list of choices depending on the game mode
if game_mode == "n" or game_mode == "normal":
    comp_choice_list = ["rock","paper","scissors"]
else:
    comp_choice_list = ["rock","paper","scissors","lizard","spock"]
# Randomly generates a choice from the chosen list above
comp_choice = random.choice(comp_choice_list)

# assigns the computers random choice with an icon and a numerical value
if comp_choice == "rock":
    comp_attack_icon = "🥔"
    game_outcome -= 3
elif comp_choice == "paper":
    comp_attack_icon = "📰"
    game_outcome -= 2
elif comp_choice == "scissors":
    comp_attack_icon = "✂"
    game_outcome -= 1
elif comp_choice == "lizard":
    comp_attack_icon = "🦎"
    game_outcome -= 4
elif comp_choice == "spock":
    comp_attack_icon = "🖖"
    game_outcome -= 5

# Display users choice vs computers choice
print(chosen_attack_icon + " vs " + comp_attack_icon)

if game_outcome == -1 or game_outcome == 4 or game_outcome == -3 or game_outcome == 2:
    print("Player Wins")
    winlosscounter.append("Win")
elif game_outcome == 1 or game_outcome == -4 or game_outcome == 3 or game_outcome == -2:
    print("CPU Wins")
    winlosscounter.append("Loss")
else:
    print("Draw")
    winlosscounter.append("Draw")

print("Player {} || Cpu {}".format(winlosscounter.count("Win"),winlosscounter.count("Loss")))

