with open("xmas.txt", "r") as f:
    input = f.read()
    f.close()

puzzle = []
for i in input.splitlines():
    puzzle.append([j for j in i])

search = "XMAS"
count = 0
mascount = 0
mas = 0

def surround(array, pos, length, diagonal=False, split=True):
    d = []

    # up down
    if not diagonal:
        tmp = []
        for i in range(pos[1]-length+1, pos[1]+length):
            if 0 <= i < len(array):
                tmp.append(array[i][pos[0]])
            else:
                tmp.append("")
        if split:
            d.append(list(reversed(tmp[:length])))
            d.append(tmp[-length:])
        else:
            d.append(tmp)
    
        # left right
        tmp = []
        for i in range(pos[0]-length+1, pos[0]+length):
            if 0 <= i < len(array[pos[1]]):
                tmp.append(array[pos[1]][i])
            else:
                tmp.append("")
        if split:
            d.append(list(reversed(tmp[:length])))
            d.append(tmp[-length:])
        else:
            d.append(tmp)

    # up-left down-right
    tmp = []
    for i in range(-length+1, length):
        if 0 <= pos[1]+i < len(array) and 0 <= pos[0]+i < len(array[1]):
            tmp.append(array[pos[1]+i][pos[0]+i])
        else:
            tmp.append("")
    if split:
        d.append(list(reversed(tmp[:length])))
        d.append(tmp[-length:])
    else:
        d.append(tmp)

    # up-right down-left
    tmp = []
    for i in range(-length+1, length):
        if 0 <= pos[1]+i < len(array) and 0 <= pos[0]+(i*-1) < len(array[1]):
            tmp.append(array[pos[1]+i][pos[0]+(i*-1)])
        else:
            tmp.append("")
    if split:
        d.append(list(reversed(tmp[:length])))
        d.append(tmp[-length:])
    else:
        d.append(tmp)

    return d

for a in range(len(puzzle)):
    for b in range(len(puzzle[a])):
        if puzzle[a][b] == search[0]:
            for c in surround(puzzle, [b, a], len(search)):
                if search in ''.join(str(d) for d in c):
                    count+=1
            
        if puzzle[a][b] == "A":
            mas = 0
            for c in surround(puzzle, [b, a], 2, split=False, diagonal=True):
                if "MAS" in ''.join(str(d) for d in c) or "SAM" in ''.join(str(d) for d in c):
                    mas+=1
            if mas == 2:
                mascount+=1
                    

print(count)
print(mascount)