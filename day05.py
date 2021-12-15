def puz1(file):
    lines = readFile(file)
    horlines = findHLines(lines)
    verlines = findVLines(lines)
    maxX = findMaxX(lines)
    maxY = findMaxY(lines)
    board = makeBoard(maxX, maxY, 0)

    board = fillHor(board, horlines)
    for line in board:
        print(line)

def puz2(file):
    pass

def fillHor(board, lines):
    for line in lines:
        print(line)
        x1 = line[0][0]
        y1 = line[0][1]
        board[y1][x1] += 1

    return board

def makeBoard(mx, my, val):
    board = []
    for y in range(mx+1):
        line = []
        for x in range(my+1):
            line += [val]
        board += [line]
    return board

def findMaxX(lines):
    max = 0
    for line in lines:
        for coord in line:
            if coord[0] > max:
                max = coord[0]
    return max

def findMaxY(lines):
    max = 0
    for line in lines:
        for coord in line:
            if coord[1] > max:
                max = coord[1]
    return max

def findHLines(lines):
    hlines = []
    for line in lines:
        if line[0][1] == line[1][1]:
            hlines += [line]

    return hlines

def findVLines(lines):
    vlines = []
    for line in lines:
        if line[0][0] == line[1][0]:
            vlines += [line]

    return vlines

def readFile(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    newlines = []
    for line in lines:
        newline = []
        coords = line.split(" -> ")
        for coord in coords:
            aPair = []
            pair = coord.split(",")
            for item in pair:
                aPair += [int(item)]
            newline += [aPair]
        newlines += [newline]
    lines = newlines

    return lines



