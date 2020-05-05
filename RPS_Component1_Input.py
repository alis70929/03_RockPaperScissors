#Rock paper scissors component 1 Input

# To do
# - Give user choice between RPS or RPSLS
# - Depending on users choice prior ask them what attack they would like to choose
# - Ask user best out of ?

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


attack_choice_valid = False
while not attack_choice_valid:
    if game_mode == "n" or game_mode == "normal":
        attack_choice = input("Please chose from Rock(R), Paper(P) or Scissors(S)").lower()
    elif game_mode == "v" or game_mode == "variant":
        attack_choice = input("Please chose from Rock(R), Paper(P), Scissors(S), Lizard(L) or Spock(Sp)").lower()

    if attack_choice == "r" or attack_choice == "rock":
        chosen_attack = "rock"
    elif attack_choice == "p" or attack_choice == "paper":
        chosen_attack = "paper"
    elif attack_choice == "s" or attack_choice == "scissors":
        chosen_attack = "scissors"
    elif game_mode == "v" or game_mode == "variant":
        if attack_choice == "l" or attack_choice == "lizard":
            chosen_attack = "lizard"
        elif attack_choice == "sp" or attack_choice == "spock":
            chosen_attack = "spock"
    else:
        continue
    print(chosen_attack)
    attack_choice_valid = True

rounds_valid = False
while not rounds_valid:
    rounds = int_checker("Best out of ?:", 1)
    if rounds % 2 == 0:
        print("Please enter an odd number above 0")
        continue
    rounds_valid = True
