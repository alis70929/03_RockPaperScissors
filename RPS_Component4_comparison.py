# Rock paper scissors component 3 - Display users choice vs computers choice

# To do
# - Use emojis to display a visual representation of user and cpu's choice
game_mode = "variant"
keepgoing = ""
while keepgoing == "":
    attack_choice_valid = False
    game_outcome = 0
    while not attack_choice_valid:
        if game_mode == "n" or game_mode == "normal":
            attack_choice = input("Please chose from Rock(R), Paper(P) or Scissors(S)").lower()
        elif game_mode == "v" or game_mode == "variant":
            attack_choice = input("Please chose from Rock(R), Paper(P), Scissors(S), Lizard(L) or Spock(Sp)").lower()

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
        else:
            continue
        attack_choice_valid = True

    # For testing purposes
    comp_choice = "paper"

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

    print(chosen_attack_icon + " vs " + comp_attack_icon)

    if game_outcome == -1 or game_outcome == 4 or game_outcome == -3 or game_outcome == 2:
        print("Player Wins")
    elif game_outcome == 1 or game_outcome == -4 or game_outcome == 3 or game_outcome == -2:
        print("CPU Wins")
    else:
        print("Draw")
