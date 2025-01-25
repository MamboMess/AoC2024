import itertools as it
import copy
import re
from sys import argv as args

f = open(args[2], "r")
rows = f.read().split("\n")

def calc(ops,t):
  nums = ops.split(".")
  while len(nums) > 1:
    a = nums.pop(0)
    op = nums.pop(0)
    b = nums.pop(0)
    if op == "+":
        c = int(a)+int(b)
        if tooHigh(c,t):
            return False
        else:
           nums.insert(0, c)     
    elif op == "*":
        c = int(a)*int(b)
        if tooHigh(c,t):
            return False
        else:
           nums.insert(0, c)
    else:
        c = str(a) + str(b)
        if tooHigh(c,t):
            return False
        else:
           nums.insert(0, c)
  return nums      

def tooHigh(c, t):
    if int(c) > int(t):
        return True

def dothing(operators, rows):
    vals = []
    for row in rows:
        t, v = row.split(": ")
        nums = v.split(" ")
        spaces = v.count(" ")
        combos = list(it.product(operators, repeat=spaces))
        ops = []
        for combo in combos:
            seq = copy.copy(v)
            for c in combo:
                x = "." + c + "."
                seq = re.sub("\s", x, seq, 1)
            ops.append(seq)
        for op in ops:
            n = calc(op, t)
            if not n:
                pass
            else:
                if int(n[0]) == int(t):
                    vals.append(int(t))
                    break
    return sum(vals)

if args[1] == "1":
	print("part1:", dothing("*+", rows))
elif args[1] == "2":
	print("part2:", dothing("*+|", rows))

f.close()
