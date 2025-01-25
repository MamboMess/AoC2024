from sys import argv as args
f = open(args[2], "r")
rows = f.read().split("\n")

maxx = len(rows[0])-1
maxy = len(rows)-1
start = ""
visit = []#make into a set

def find(rows):
    for y, col in enumerate(rows):
      for x, i in enumerate(col):
        if i == "^" or i == ">" or i == "<" or i == "v":
           return (i,y,x)
           
def inRange(pos):  
    i,y,x = pos
    if y >= 0 and x >= 0 and y < maxy and x < maxx:
        return True

def notObj(rows, pos):
    i,y,x = pos
    if rows[y][x] != "#":
        return True  
    else:
        return False 

def next(pos):
    i,y,x = pos
    step = i,y,x
    if i == "^":
        step = i,y-1, x
    elif i == ">":
        step = i,y,x+1
    elif i == "v":
        step = i,y+1,x
    elif i == "<":
        step=i,y,x-1
    return step
        
def turn(pos):
    i,y,x = pos
    if i == "^":
        i = ">"
    elif i == ">":
        i = "v"
    elif i == "v":
        i = "<"
    elif i == "<":
        i = "^"
    pos = (i,y,x)
    return pos

start = find(rows)
visit.append(start)
i,y,x = start
pos = i,y,x
while inRange(pos):
    step = next(pos)
    if notObj(rows,step):
      pos = step
      visit.append(pos)
    else:
      pos = turn(pos)
      visit.append(pos)

visited = []    
for i,y,x in visit:
    visited.append((y,x))

if args[1] == "1":
	print("part1: ", len(set(visited)))
elif args[1] == "2":
		visited.pop(0)
		blocks = []
		for y, col in enumerate(rows):
			  for x, i in enumerate(col):
				  if i == "#":
					  blocks.append((y,x))
		looped = 0
		loopers = []
		for a in set(visited):
			objs = blocks + [a]
			start = find(rows)
			i,y,x= start
			pos = i,y,x
			visit = []
			while inRange(pos):
				step = next(pos)
				if step not in visit:
					if (step[1], step[2]) not in objs:
						pos = step
						visit.append(pos)
					else:
						pos = turn(pos)
						visit.append(pos)
				elif step in loopers:
					looped += 1
					loopers.extend(visit)
					break
				else:
					looped += 1
					loopers.extend(visit)
					break
				  
		print("part2:", looped)
f.close()
