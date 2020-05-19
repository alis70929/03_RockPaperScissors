# RPS component 7 Endgame summary and ask if the player wants to play again

keepgoin = ""
while keepgoin == "":
    win_loss_rounds = ["win", "loss", "loss"]
    win_loss_overall = "loss"
    list_count = 0
    print("Round # || Win/Loss")
    for item in win_loss_rounds :


        print("Round {} || {}    ".format(list_count + 1, win_loss_rounds[list_count]))
        list_count += 1
    print("")
    print("Overall  || {}".format(win_loss_overall))
    keepgoin = input("Press <enter> to play again or press any key then <enter> to quit")
