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
                            return scoreBoard(board, int(ball))

    for i, board in enumerate(boards):
        print("----", i, "----")
        for line in board:
            print(line)

def puz2(file):
    balls, boards = buildGame(file)
    print(balls)

    for ballNum, ball in enumerate(balls):
        print()
        print("--Ball--", ball, "------------")
        for b, board in reversed(list(enumerate(boards))):
            for l, line in enumerate(board):
                for i, item in enumerate(line):
                    if item == int(ball):
                        boards[b][l][i] = "X"
                        if testBoard(board):
                            if len(boards)>1:
                                boards.remove(board)
                            else:
                                return scoreBoard(board, ball)




        for i, board in enumerate(boards):
            print("--board--", i, "----")
            for line in board:
                print(line)


def testBoard(board):
    for y, line in enumerate(board):
        if line == ["X", "X", "X", "X", "X"]:
            print("Found Horizontal", y)
            return True
    for x, item in enumerate(board[0]):
        if item == "X":
            win = True
            for i in range(5):
                if board[i][x] != "X":
                    win = False
                    break
            if win:
                print("Found Vertical", x)
                return True
    return False


def scoreBoard(board, ball):
    sum = 0
    for line in board:
        for i in line:
            if i != "X":
                sum += int(i)
    print(sum, ball)
    return (sum*int(ball))


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

