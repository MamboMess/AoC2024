
f = open("input.txt", "r")
lines = f.read().split("\n")
left = []
right = []
for i in lines:
   x = i.split("   ")
   left.append(int(x[0]))
   right.append(int(x[1]))


left.sort()
right.sort()
diffs = []
for n, i in enumerate(left):
    d = abs(i - right[n])
    diffs.append(d)
print("part 1:", sum(diffs)) #part 1

scores = []
for i in left:
   c = right.count(i)
   scores.append(i * c)
print("part1:", sum(scores)) #part 2
f.close()