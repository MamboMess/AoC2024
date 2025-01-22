from sys import argv as args


def inRange(y,x):
    if y >= 0 and x >= 0 and y < maxy and x < maxx:
        return True
    else:
        return False
        
def getAdj(y,x,z):
    adj = [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]
    adj = [i for i in adj if inRange(i[0], i[1]) and int(m[i[0],i[1]])-1 == int(z)]
    return adj


f = open(args[2],"r")

map = f.read().split("\n")
m = {}
zeros = {}
nines = []
maxx = len(map[0])
maxy = len(map)
for y, row in enumerate(map):
     for x, col in enumerate(row):
         m[(y,x)] = col
         if col == "9":
             nines.append((y,x))
         elif col == "0":
             zeros[(y,x)] = []

total = []
ranks = []
for y,x in zeros:
  visited = []
  peaks= []
  adj = getAdj(y,x, m[y,x])
  for a in adj:
      if a not in visited:
          visited.append(a)
  while len(visited) > 0:
      n1,n2 = visited.pop()
      if m[n1,n2] == "9":
          peaks.append((n1,n2))
      else:
          nodes = getAdj(n1,n2,m[n1,n2])
          if len(nodes) != 0:
            for nod in nodes:
              if nod not in visited:
                  visited.append(nod)
  if args[1] == "1":
  	total.append(len(set(peaks)))
  elif args[1] == "2":
  	ranks.append(len(peaks))

if args[1] == "1":
  print("part1:", sum(total))
elif args[1] == "2":
  print("part2:", sum(ranks))

f.close()
