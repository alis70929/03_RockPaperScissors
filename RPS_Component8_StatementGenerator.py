# RPS Component 8 Statement generator

# To do
# - Make a function that makes statements look nice

# Functions go here
def rps_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char * len(statement))
    print()

# Main code goes here
rps_statement("--- No one won this round, It was a draw ---", "-")
rps_statement("!!! You won this round, Well Done !!!", "!")
rps_statement("xxx You lost this round, better luck next round xxx", "x")
rps_statement("### Round 1 ###", "#")
