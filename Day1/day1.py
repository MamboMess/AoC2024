#!/usr/bin/env python3
import sys

f = open(sys.argv[2], "r")
lines = f.read().split("\n")
left = []
right = []
for i in lines:
   x = i.split("   ")
   left.append(int(x[0]))
   right.append(int(x[1]))

left.sort()
right.sort()

if sys.argv[1] == "1":
		diffs = []
		for n, i in enumerate(left):
			d = abs(i - right[n])
			diffs.append(d)
		print("part 1:", sum(diffs)) #part 1

elif sys.argv[1] == "2":
		scores = []
		for i in left:
		   c = right.count(i)
		   scores.append(i * c)
		print("part 2:", sum(scores)) #part 2

f.close()
