
f = open("input.txt", "r")
input = f.read().split("\n")

maxx = len(input[0])
maxy = len(input)
visited = []

def inRange(i):
    y,x = i
    if y >= 0 and x >= 0 and y < maxy and x < maxx:
        return True
    else:
        return False
        
def findSides(y,x):
    sides = [(y-1, x),(y,x+1),(y+1,x),(y,x-1)]
    return sides

def isType(a,i):
    y,x = a
    if input[y][x] == i:
        return True
    else:
        return False

def flood(y,x):
    roi = [(y,x)]
    ii = input[y][x]
    adj = findSides(y,x)
    adj = [i for i in adj if i not in visited and i not in roi and inRange(i) and isType(i, ii)]
    while len(adj) > 0:
        a = adj.pop(0)
        if a in visited:
            pass
        else:
           ai = input[a[0]][a[1]]
           visited.append(a)
           roi.append(a)
           adj2 = findSides(a[0],a[1])
           adj2 = [i for i in adj2 if i not in visited and i not in roi and inRange(i) and isType(i, ai)]
           adj.extend(adj2)
    return(roi)

def roiPrice(roi):
    sides = 0
    for i in roi: 
      y,x = i
      adj = findSides(y,x)
      adj2 =  [i for i in adj if inRange(i) and isType(i, input[y][x])]
      sides += len(adj) - len(adj2)
    price = sides * len(roi)
    return price, sides
      
def findEdges(roi):
    edges= []
    N = []
    E = []
    S = []
    W = []
    for i in roi: 
      y,x = i
      adj = findSides(y,x)
      sides = []
      for n, a in enumerate(adj):
          if not inRange(a) or not isType(a, input[y][x]):
              sides.append(True)
          else:
              sides.append(False)
      if any(sides):
          edges.append(i)
      if sides[0] or sides[2]:
          N.append(i)
      if sides[1] or sides[3]:
          E.append(i)
      if sides[0] or sides[2]:
          S.append(i)
      if sides[1] or sides[3]:
          W.append(i)
    return N, S,E,W

regions= []
q = []
start = (0,0)
plots = {}
for y, col in enumerate(input):
  for x, i in enumerate(col):
     if (y,x) not in visited:
         visited.append((y,x))
         region = flood(y,x)
         if i not in plots:
             plots[i] = []
         plots[i].append(set(region))

prices = []
for p, ls in plots.items():
   for roi in ls:
      price, sids = roiPrice(roi)
      prices.append(price)

print("pt1: ", sum(prices))
f.close()