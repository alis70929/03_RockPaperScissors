# Rock paper scissors component 2 - Computer Attack Choice Generator

# To Do
# - Depending on what game_mode the user has chosen generate a choice.

# Imports
import random
# Main code
# Sets game mode for testing purposes
game_mode = "normal"
if game_mode == "n" or game_mode == "normal":
    comp_choice_list = ["rock","paper","scissors"]
else:
    comp_choice_list = ["rock","paper","scissors","lizard","spock"]
for item in range(0,10):
    comp_choice = random.choice(comp_choice_list)
    print(comp_choice)

