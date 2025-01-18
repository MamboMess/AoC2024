
f = open("input.txt", "r")
map, path = f.read().split("\n\n")
path = path.replace("\n", "")
map = map.split("\n")

map = [list(i) for i in map]
maxx = len(map[0])
maxy = len(map)

def look(p,y,x):
    if p == '^':
        y = y - 1
    elif p == '>':
        x = x + 1
    elif p == 'v':
        y = y + 1
    elif p == '<':
        x = x - 1
    return (y,x)

def move(p,y,x):
    global map
    a,b = look(p,y,x)
    if map[a][b] == '#':
        return map
    elif map[a][b] == 'O':
        searchline(p,y,x, a,b)
        return map
    elif map[a][b] == '.':
        map[y][x] = '.'
        map[a][b] = '@'
        return map
        
def findbot(arr):
   for y,row in enumerate(arr):
      for x,col in enumerate(row):
           if col == '@':
              return (y,x)
              
def checkline(line):
    global map
    check = False
    for y,x in line:
      if map[y][x] == '.' or map[y][x] == '#':
        check = True
        break
    return check
            
def searchline(p,y,x,a,b):
    line = [(y,x),(a,b)]
    while not checkline(line):
         n = look(p,a,b)
         line.append(n)
         a,b = n[0],n[1]     
    c,d = line[-1]
    if map[c][d] != "#":
       dot = line.pop(-1)
       o = line.pop(1)
       guy = line.pop(0)
       map[dot[0]][dot[1]] = 'O'
       map[guy[0]][guy[1]] = '.'
       map[o[0]][o[1]] = "@"
 
y,x = findbot(map)    
for p in path:
   move(p,y,x)
   y,x = findbot(map)

gps = []                        
for y,row in enumerate(map):
    for x,col in enumerate(row):
        if col == "O":
            pts = (y*100) + x
            gps.append(pts)

print(sum(gps))
f.close()