#RPS Component 1 Normal

# To do
# - Get choice of attack from user, make sure its valid in this scenario(Rock Paper or Scissors)
# - Get how many rounds user wishes to play, Make sure its an int over 0 and odd

#functions go here
def choose_attack(question,error):
    valid = False

    while not valid:
        response = input(question)

        if response.lower() == "scissors" or response.lower() == "s":
            choosing_attack = "scissors"
            return choosing_attack
        elif response.lower() == "rock" or response.lower() == 'r':
            choosing_attack = "rock"
            return choosing_attack
        elif response.lower() == "paper" or response.lower() == "p":
            choosing_attack = "paper"
            return choosing_attack
        else:
            print(error)

def intcheck_odd(question,low ):
    valid = False

    # Error message
    error = "Please enter a whole number equal to or above {} ".format(low)
    while not valid:
        try:
            # Gets user input
            response = int(input(question))
            # Checks number is not too low
            if response < low:
                print(error) # If its too low  display error
                continue
            if response % 2 == 0:  # Checks if number is odd
                print("Please enter an odd number") # If odd displays an unique error
                continue

            return response
        # If input is not a number or is a decimal then display error
        except ValueError:
            print(error)
            print()


# Main Code goes here
keepgoing = ""
while keepgoing == "":
    chosen_attack = choose_attack("Choose Rock(R), Paper(P) or Scissors(S)", "Please check your spelling and try again")
    rounds = intcheck_odd("Best out of ?:",1)
    print(rounds)


