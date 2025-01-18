from itertools import pairwise
import copy

file = open("input.txt", "r")
data = file.read().split("\n")
data = [d.split(" ") for d in data]

safe1 = 0
safe2 = 0

def test1(row):
    dir = []
    for a, b in pairwise(row):
        if a != b:
            dir.append("down") if a > b else dir.append("up")
    ups = dir.count("up")
    downs = dir.count("down")
    if ups == len(row) - 1 or downs == len(row) - 1:
        return True

def test2(row):
    for a, b in pairwise(row):
        if abs(a - b) > 3 or abs(a-b) == 0:
           return False
    return True

def popOne(row):
    for n, i in enumerate(row):
        row2 = copy.copy(row)
        row2.pop(n)
        if test1(row2) and test2(row2):
           return True
        else:
            pass
    return False

for row in data: #part1
    row = [int(r) for r in row]
    if test1(row) and test2(row):
        safe1 += 1    
print("part1: ", safe1) 

for row in data: #part2
    row = [int(r) for r in row]
    if test1(row) and test2(row):
        safe2 += 1
    else:
        if popOne(row):
            safe2 += 1
print("part2: ",safe2)
file.close()