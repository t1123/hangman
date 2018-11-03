def hangman(word):
    wrong = 0
    stages = ["",
              "______    ",
              "|         ",
              "|     |   ",
              "|     0   ",
              "|    /|\  ",
              "|    / \  ",
              "|         "
              ]
    rletter = list(word)
    board = ["_"] * len(word)
    win = False
    print("welcome to hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        mag = "input 1 character:"
        char = input(mag)
        if char in rletter:
            cind = rletter.index(char)
            board[cind] = char
            rletter[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You won")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("you lost.answer is {}".format(word))

import random
qlist = ["march","beauty","happy","sunny","peace","beat","rhythm","melody","muse","moonlight","miracle","magical","yell","ange","amour","heart","sword","diamond","rosseta","ace","passion"]
s = random.randint(0,20)
ans = qlist[s]

hangman(ans)
