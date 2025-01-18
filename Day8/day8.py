from itertools import combinations

f = open("input.txt", "r")
rows = f.read().split("\n")

ants = {}
maxx = len(rows[0]) 
maxy = len(rows) 

def inRange(node):
    y,x = node
    if y >= 0 and x >= 0 and y < maxy and x < maxx:
        return node
    else:
        return False

def getAllNodes(a,b):
   nodes = []
   y1, x1 = a
   y2, x2 = b
   top = a if y1 < y2 or y1 == y2 and x1 < x2 else b
   bot = a if top != a else b
   while inRange(top):
      nodes.append(top)
      topnode = (top[0] - (y2-y1), top[1] - (x2-x1))
      top = topnode
   while inRange(bot):
      nodes.append(bot)
      botnode = (bot[0] + (y2-y1), bot[1] + (x2-x1))
      bot = botnode
   return nodes
                   
def getNodes(a,b):
   nodes = []
   y1, x1 = a
   y2, x2 = b
   top = a if y1 < y2 or y1 == y2 and x1 < x2 else b
   bot = a if top != a else b
   topnode = (top[0] - (y2-y1), top[1] - (x2-x1))
   botnode = (bot[0] + (y2-y1), bot[1] + (x2-x1))
   if inRange(topnode):
       nodes.append(topnode)
   if inRange(botnode):
       nodes.append(botnode)
   return nodes
                    
for y, row in enumerate(rows):
    for x, col in enumerate(row):
        if col != ".":
          if col not in ants:
            ants[col] = [(y,x)]
          else:
            ants[col].append((y,x))

                
allnodespt1 = []
allnodespt2=[]

for key, val in ants.items():
    combos = list(combinations(val,2))#get pairs of each antenna with no repeats
    antinodes1 = []
    antinodes2 = []
    for a,b in combos:
        nodes = getNodes(a,b)
        antinodes1.extend(nodes)
        nodes = getAllNodes(a,b)
        antinodes2.extend(nodes)
    for i in set(antinodes1):
        allnodespt1.append(i)
    for i in set(antinodes2):
        allnodespt2.append(i)   
                  
print("pt1: ", len(set(allnodespt1)))
print("pt2: ", len(set(allnodespt2)))

f.close()