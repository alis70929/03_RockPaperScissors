#Rock paper scissors component 1 Input

# To do
# - Give user choice between RPS or RPSLS
# - Depending on users choice prior ask them what attack they would like to choose
# - Ask user best out of ?

# Functions go here
def int_checker(question):

    try:
        response = int(input(question))
    except ValueError:
        print("Please enter a whole number")
    return response

# Main code

game_mode_valid = False
while not game_mode_valid:
    # Ask user which game mode they would like to play
    game_mode = input("Normal(N) or Variant(V)?").lower()

    # Give user confirmation on which game mode they have chosen
    if game_mode == "n" or "normal":
        print("You have chosen normal rules for rock paper scissors")
        game_mode_valid = True
    elif game_mode == "v" or "variant":
        print("You have chosen normal rules for rock paper scissors")
        game_mode_valid = True
    # If user inputs anything other than the given choices print an error message
    else:
        print("Please choose either Normal(N) or Variant(V) rules")

attack_choice_valid = False
while not attack_choice_valid:
    if game_mode == "n" or "normal":
        attack_choice = input("Please chose from Rock(R), Paper(P) or Scissors(S)").lower()
    elif game_mode == "v" or "variant":
        attack_choice = input("Please chose from Rock(R), Paper(P), Scissors(S), Lizard(L) or Spock(Sp)").lower()

    if attack_choice == "r" or "rock":
        chosen_attack = "rock"
    elif attack_choice == "p" or "paper":
        chosen_attack = "paper"
    elif attack_choice == "s" or "scissors":
        chosen_attack = "scissors"
    elif game_mode == "v" or "variant":
        if attack_choice == "l" or "lizard":
            chosen_attack = "lizard"
        elif attack_choice == "sp" or "spock":
            chosen_attack = "spock"
    else:
        continue
    print(attack_choice)
    attack_choice_valid = True

rounds_valid = False
while not rounds_valid:
    rounds = int_checker("Best out of ?:")
    if rounds % 2 == 0:
        print("Please enter an odd number")
        continue
    rounds_valid = True
