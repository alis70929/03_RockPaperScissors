# RPS Component 2 Random Choice Generator

# To Do
# - Make the code choose rock paper or scissors randomly

# Imports here
import random


# Main code here

# Computer randomly chooses an attack
attack_choices = ["rock","paper","scissors","lizard","spock"]
for item in range (0,10):
    comp_chosen_attack = random.choice(attack_choices)
    print(comp_chosen_attack)
