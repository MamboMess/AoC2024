import re
from sys import argv as args
f = open(args[2], "r")

if args[1] == "2":
	raise NotImplementedError("P2 not implemented")

file = f.read().split("\n\n")
file = [i.split("\n") for i in file]
games = []
acost = 3
bcost = 1
for i in file:
    nuns = []
    claw = {}
    for j in i:
     n = re.findall("\d+",j)
     nuns.append(n)
    claw['a'] = (int(nuns[0][0]),int(nuns[0][1]))
    claw['b'] = (int(nuns[1][0]),int(nuns[1][1]))
    claw['prize'] = (int(nuns[2][0]),int(nuns[2][1]))
    games.append(claw)

def maxpress(x,y,ax,ay,bx,by):
    maxa = 100
    maxb = 100
    if maxa*ax > x:
        maxa = int(x/ax) if int(x/ax) < maxa else maxa
    if maxa*ay > y:
            maxa = int(y/ay) if int(y/ay) < maxa else maxa
    if maxb*bx > x:
        maxb = int(x/bx) if int(x/bx) < maxb else maxb
    if maxb*by > y:
            maxb = int(y/by) if int(y/by) < maxb else maxb
    return (maxa,maxb)

def multiple(m,n):
    return True if m % n == 0 else False
     
def findmatch(maxa,maxb,x,y,ax,ay,bx,by,scores):
    r = x - (maxa*ax)
    if maxa > 0:
      if multiple(r,bx):
        bpress = r/bx
        if reachprize(maxa,bpress,x,y,ax,ay,bx,by):
          score = getscore(maxa,bpress)
          return score

def reachprize(apress, bpress,x,y,ax,ay,bx,by):
     check = True
     totx = int((apress*ax) + (bpress*bx))
     toty = int((apress*ay) + (bpress*by))
     if not totx == x:
         check = False
     if not toty == y:
         check = False
     return check
         
def getscore(ap,bp):
    pts = (ap*3)+(bp*1)  
    return pts
      
t = [ i for i in range(100)]
pairs = []
for n in t:
    pairs.append((n,100-n))

tokens = []
for claw in games:
    x,y = claw['prize'][0],claw['prize'][1] 
    ax, ay = claw['a'][0],claw['a'][1]
    bx,by = claw['b'][0],claw['b'][1]
    maxa,maxb = maxpress(x,y,ax,ay,bx,by)
    #print(maxa,maxb)
    scores = []
    while maxa > 0:
      s = findmatch(maxa,maxb,x,y,ax,ay,bx,by,scores)
      if s is not None:
        scores.append(s)
      maxa -= 1
    if len(scores) != 0:
      tokens.append(min(scores))

print(int(sum(tokens)))
f.close()
