def puz1(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    newlines = []
    for line in lines:
        newline = int(line)
        newlines += [newline]
    lines = newlines

    count = 0
    for i, line in enumerate(lines):
        if i == 0:
            pass
        elif line > lines[i-1]:
            count += 1

    print(count)

def puz2(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    newlines = []
    for line in lines:
        newline = int(line)
        newlines += [newline]
    lines = newlines



    count = 0
    sum = 0
    oldsum = 0
    for i, line in enumerate(lines):
        print(i, oldsum, sum)
        oldsum = sum
        if i < 2:
            pass
        elif i == 2:
            sum = line + lines[i - 1] + lines[i - 2]
        else:
            sum = line + lines[i-1]+lines[i-2]
            if sum > oldsum:
             count += 1
    print(count)