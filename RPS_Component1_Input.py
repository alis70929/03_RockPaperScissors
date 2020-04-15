#RPS Component 1 Normal

# To do
# - Get choice of attack from user, make sure its valid in this scenario
# - Get how many rounds user wishes to play, Make sure its an int over 0 and odd

#functions go here
def ChooseAttack(question,error):
    valid = False

    while not valid:
        response = input(question)

        if response.lower() == "scissors" or "s":
            ChosenAttack = "scissors"
            return ChosenAttack
        elif response.lower() == "rock" or 'r':
            ChosenAttack = "rock"
            return ChosenAttack
        elif response.lower() == "paper" or "p":
            ChosenAttack = "paper"
            return ChosenAttack
        else:
            print(error)

# Main Code goes here
ChosenAttack = ChooseAttack("Choose Rock, Paper or Scissors", "Please check your spelling and try again")
