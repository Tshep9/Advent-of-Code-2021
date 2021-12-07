def puz1(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    newlines = []
    for line in lines:
        newline = line.strip("\n")
        newlines += [newline]
    lines = newlines

    counts = []
    for c in lines[0]:
        counts += [0]


    print(counts)

    for line in lines:
        for i, b in enumerate(line):
            if b == "1":
                counts[i] += 1

    print(counts)

    gamma = ""
    epsilon = ""
    for n in counts:
        if n > len(lines)/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(gamma, int(gamma,2), epsilon, int(epsilon,2), int(gamma,2)*int(epsilon,2))