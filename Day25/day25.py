import numpy as np
from sys import argv as args

if args[1] == "2":
	raise NotImplementedError("Part 2 not implemented for Day 25")

f = open(args[2], "r")
input = f.read().split("\n\n")
input = [i.split("\n") for i in input]

def islock(arr):
    row = []
    for i in arr[0]:
        if i == "#":
            row.append(True)
        else:
            row.append(False)
    return True if all(row) else False

def county(arr):
   pins = []
   if islock(arr):
     for n,x in enumerate(arr[0]):
       l = arr[1:,n].tolist()
       p = l.count("#")
       pins.append(p)
   else:
     for n,x in enumerate(arr[0]):
       l = arr[:-1,n].tolist()
       p = l.count("#")
       pins.append(p)
   return pins

def fits(key,lock):
    pairs = zip(key,lock)
    test = []
    for a,b in pairs:
       if a + b < 6:
           test.append(True)
       else:
           break
    return True if len(test) == 5 else False
locks = []
keys = []
for n,i in enumerate(input):
    arr = [list(x) for x in i]
    arr = np.array(arr)
    pins = county(arr)
    if islock(arr):
       locks.append(pins)
    else:
       keys.append(pins)

fit = 0              
for key in keys:
    for lock in locks:
        if fits(key,lock):
            fit += 1      

print("part1:", fit)
f.close()
