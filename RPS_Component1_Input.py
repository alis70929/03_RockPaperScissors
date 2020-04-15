#RPS Component 1 Normal

# To do
# - Get choice of attack from user, make sure its valid in this scenario
# - Get how many rounds user wishes to play, Make sure its an int over 0 and odd

#functions go here
def choose_attack(question,error):
    valid = False

    while not valid:
        response = input(question)

        if response.lower() == "scissors" or response.lower() == "s":
            ChosenAttack = "scissors"
            return ChosenAttack
        elif response.lower() == "rock" or response.lower() == 'r':
            ChosenAttack = "rock"
            return ChosenAttack
        elif response.lower() == "paper" or response.lower() == "p":
            ChosenAttack = "paper"
            return ChosenAttack
        else:
            print(error)

def intcheck_odd(question,low = None,high = None):
    valid = False
    # Error messages
    if low is not None and high is not None: # Error message if variables are given
        error = "Please enter a whole number between {} and {} (Inclusive) ".format(low,high)
    elif low is not None and high is None: # Error message if only low variable is given
        error = "Please enter a whole number equal to or above {} ".format(low)
    elif low is not None and high is None: # Error message if only high variable is given
        error = "Please enter a whole number equal to or below {} ".format(high)
    else: # Error message if no variables are given
        error = "please enter a whole number"


    while not valid:
        try:
            # Gets user input
            response = int(input(question.format(low, high)))
            # Checks number is not too low
            if low is not None and response < low:
                print(error) # If its too low  display error
                continue
            # Checks number is not too high
            if high is not None and response > high:
                print(error)  # If it is too high print error
                continue
            if response % 2 == 0:  # Checks if number is odd
                print("Please enter an odd number")
                continue

            return response
        # If input is not a number or is a decimal then display error
        except ValueError:
            print(error)
            print()


# Main Code goes here
keepgoing = ""
while keepgoing == "":
    chosen_attack = choose_attack("Choose Rock, Paper or Scissors", "Please check your spelling and try again")
    rounds = intcheck_odd("Best out of ?:",1)
    print(rounds)


