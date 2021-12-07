def puz1(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    newlines = []
    for line in lines:
        d = line.split(" ")[0]
        v = line.split(" ")[1]
        newline = {"d":d, "v":int(v)}
        newlines += [newline]
    lines = newlines

    x = 0
    y = 0
    for line in lines:
        if line["d"] == "forward":
            x += line["v"]
        elif line["d"] == "down":
            y += line["v"]
        elif line["d"] == "up":
            y -= line["v"]
        else:
            print("OMG")
    print(x,y,x*y)

def puz2(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    newlines = []
    for line in lines:
        d = line.split(" ")[0]
        v = line.split(" ")[1]
        newline = {"d":d, "v":int(v)}
        newlines += [newline]
    lines = newlines

    x = 0
    y = 0
    aim = 0
    for line in lines:
        if line["d"] == "forward":
            x += line["v"]
            y += aim * line["v"]
        elif line["d"] == "down":
            aim += line["v"]
        elif line["d"] == "up":
            aim -= line["v"]
        else:
            print("OMG")
    print(x,y,x*y)