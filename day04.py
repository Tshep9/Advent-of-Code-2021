def puz1(file):
    balls, boards = buildGame(file)
    print(balls)

    for ball in balls:
        print("---------", ball, "------------")
        for b, board in enumerate(boards):
            for l, line in enumerate(board):
                for i, item in enumerate(line):
                    if item == int(ball):
                        boards[b][l][i] = "X"
                        if testBoard(board):
                            scoreBoard(board, int(Ball))

    for i, board in enumerate(boards):
        print("----", i, "----")
        for line in board:
            print(line)

def testBoard(board):
    for y, line in enumerate(board):
        if line == ["X", "X", "X", "X", "X"]:
            print("Found Horizontal")
            return True
    for x, item in enumerate(board[0]):
        if item == "X":
            win = True
            for i in range(5):
                if board[i][x] != "X":
                    win = False
                    break
            if win:
                print("Found Vertical")
                return True
    return False





def buildGame(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    newlines = []
    for line in lines:
        newline = line.strip("\n")
        newlines += [newline]
    lines = newlines

    balls = lines[0].split(',')
    lines.remove(lines[0])
    lines.remove(lines[0])

    #print(balls)
    boards = []
    board = []
    for line in lines:
        if line == "":
            boards += [board]
            board = []
        else:
            theLine = line.split(" ")
            boardLine = []
            for i in theLine:
                if i != "":
                    boardLine += [int(i)]
            board += [boardLine]
    boards += [board]

    return balls, boards

