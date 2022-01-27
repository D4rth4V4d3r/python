def gameison(input_szam):
    global in_game
    global trynumber

    if input_szam == random_game:
        print("WIN")
        game_on = False
    elif input_szam > random_game:
        print("The random number is smaller")
        trynumber -=2
    elif input_szam < random_game:
        print("The random number is bigger")
        trynumber -=2	