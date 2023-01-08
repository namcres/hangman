import random


def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|      |        ",
              "|      |        ",
              "|      0        ",
              "|     /|\       ",
              "|     / \       ",
              "|_________      "]
    rletters = list(word)
    gletters = list()
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        print(" ".join(board))
        print("\nWrong letters:\n", gletters)
        msg = "\nGuess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            gletters.append(char)
            wrong += 1
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: e]))
        print("You lose! It was {}.".format(word))


words = ["aardvark", "apple", "candy", "blashpemous", "cartesian",
         "celebrate", "zoo", "market", "farmer", "house", "clandestine",
         "party", "google", "goggle", "state", "bed"]
randIndex = random.randint(0, len(words))
randWord = words[randIndex]
hangman(randWord)
