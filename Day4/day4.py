import copy

f = open("input.txt")
data = f.read().split('\n')

maxx = len(data[0])
maxy = len(data)
xmas = 0

def inRange(x, y, coords):
    letters = []
    for a,b in coords:
        if a >= 0 and b >= 0 and a < maxx and b < maxy:
          letters.append(data[b][a])
    if isMAS(letters):
        return True

def isMAS(ls):
    if len(ls) == 3 and ls[0] == "M" and ls[1] == "A" and ls[2] == "S":
        return True

def isxMAS(x,y):
    coords = [(x-1, y+1), (x+1,y+1), (x+1,y-1), (x-1,y-1)]
    letters= []
    for x,y in coords:
        if x >= 0 and y >= 0 and x < maxx and y < maxy:
            letters.append(data[y][x])
        else:
            letters.append(".")
    if (letters[0] + letters[2] == "MS" or letters[0] + letters[2] == "SM") and (letters[1] + letters[3] == "MS" or letters[1] + letters[3] == "SM"):
        return True

for y, i in enumerate(data): ##pt1
    for x, j in enumerate(i):
        if j == "X":
            upcoords = [(x, y-1), (x,y-2), (x,y-3)]
            dcoords = [(x,y+1),(x,y+2),(x,y+3)]
            lcoords = [(x-1,y),(x-2,y),(x-3,y)]
            rcoords = [(x+1,y),(x+2,y),(x+3,y)]
            uprcoords = [(x+1,y+1),(x+2,y+2),(x+3,y+3)]
            uplcoords = [(x-1,y+1),(x-2,y+2),(x-3,y+3)]
            dlcoords = [(x-1,y-1),(x-2,y-2),(x-3,y-3)]
            drcoords = [(x+1,y-1),(x+2,y-2),(x+3,y-3)]
            if inRange(x,y,upcoords):
                xmas += 1 
            if inRange(x,y,dcoords):
                xmas += 1
            if inRange(x,y,lcoords):
                xmas += 1
            if inRange(x,y,rcoords):
                xmas += 1
            if inRange(x,y,uplcoords):
                xmas += 1
            if inRange(x,y,uprcoords):
                xmas += 1
            if inRange(x,y,dlcoords):
                xmas += 1
            if inRange(x,y,drcoords):
                xmas += 1

print("part1:", xmas)

xmas2 = 0
for y, i in enumerate(data): #p2
    for x, j in enumerate(i):
        if j == "A":
            if isxMAS(x,y):
                xmas2 += 1
print("part2:", xmas2)
f.close()