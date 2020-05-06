
rounds = int(input("Best of ?:"))
rounds_needed_to_win = (rounds // 2) + 1
print("{} Rounds needed to win".format(rounds_needed_to_win))
rounds_played = 0
winlosscounter = []

while winlosscounter.count("Win") < rounds_needed_to_win and winlosscounter.count("Loss") < rounds_needed_to_win:
    rounds_played += 1
    print("Round {}".format(rounds_played))
    win_or_lose = input("win or lose?")



    if win_or_lose == "win":

        winlosscounter.append("Win")
    elif win_or_lose == "lose":

        winlosscounter.append("Loss")
    else:

        winlosscounter.append("Draw")

    print("Player {} || Cpu {}".format(winlosscounter.count("Win"),winlosscounter.count("Loss")))

if winlosscounter.count("Win") == rounds_needed_to_win:
    print("Player wins the match")
else:
    print("Cpu wins the match")
