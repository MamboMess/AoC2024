
f = open("input.txt", "r")
lines = f.read().split("\n")

robots = []
w = 101
h = 103

def inRange(x,y):
    if x < 0:
        x = w + x
    elif x >= w:
        x = x - w
    else:
        x = x
    if y < 0:
        y = h + y
    elif y >= h:
        y = y - h
    else:
        y = y
    return x,y

def move(v,p):
    vx,vy = v
    x,y = p
    px,py = x+vx,y+vy
    p = inRange(px,py)  
    return(p) 

def inquad(x,y):
    if x == int(w/2) or y == int(h/2):
        return "ignore"
    else:
     if x < int(w/2):
        if y < int(h/2):
            return "q1"
        else:
            return "q3"
     elif x > int(w/2):
         if y < int(h/2):
             return "q2"
         else:
             return "q4"
             
def countguards(bots):
    quad = {}
    for b in bots:
        x = b[1][0]
        y = b[1][1]
        key = inquad(x,y)
        if key not in quad:
            quad[key] = 1
        else:
            quad[key] += 1
    return quad


for line in lines:
    line = line.split(" ")
    line = [i.split("=") for i in line]
    line = [i[1].split(",") for i in line]
    p = (int(line[0][0]),int(line[0][1]))
    v = (int(line[1][0]),int(line[1][1]))
    robots.append([v,p])

secs = 100
mm = (2,4)
vv = (2,-3)

while secs > 0:
  for n,v in enumerate(robots):
    p = move(v[0],v[1])
    robots[n][1] = p
  secs -= 1

quads = countguards(robots)
tot = 1
for k,v in quads.items():
    if k != "ignore":
        tot = tot * v

print("part1:", tot)
f.close()