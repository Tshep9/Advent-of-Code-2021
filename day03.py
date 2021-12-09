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

def puz2(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    newlines = []
    for line in lines:
        newline = line.strip("\n")
        newlines += [newline]
    lines = newlines
    data = lines

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
        if n >= len(lines)/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(counts)
    print(gamma)

    lines = data
    pos = 0
    while len(lines)>1:
        counts = []
        for c in lines[0]:
            counts += [0]
        for line in lines:
            for i, b in enumerate(line):
                if b == "1":
                    counts[i] += 1

        print(counts)

        gamma = ""
        for n in counts:
            if n >= len(lines) / 2:
                gamma += "1"
            else:
                gamma += "0"
        print(gamma)
        newLines = []
        for line in lines:
            if line[pos] == gamma[pos]:
                newLines += [line]
        lines = newLines
        pos+=1

        print(pos, lines)

    o2= lines[0]
    lines = data
    pos = 0
    while len(lines)>1:
        counts = []
        for c in lines[0]:
            counts += [0]
        for line in lines:
            for i, b in enumerate(line):
                if b == "1":
                    counts[i] += 1

        print(counts)

        epsilon = ""
        for n in counts:
            if n >= len(lines) / 2:
                epsilon += "0"
            else:
                epsilon += "1"
        print(epsilon)
        newLines = []
        for line in lines:
            if line[pos] == epsilon[pos]:
                newLines += [line]
        lines = newLines
        pos+=1

        print(pos, lines)
    co2 = lines[0]

    print(o2, int(o2, 2), co2, int(co2, 2), int(o2, 2) * int(co2, 2))