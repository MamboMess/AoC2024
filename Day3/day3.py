
f = open("input.txt","r")
a = f.read()
data = a.split("mul")

def isvalid(i):
    if len(i) < 5:
        return False
    elif i[0] != "(":
        return False
    elif ")" not in i:
        return False
    elif "," not in i:
        return False
    else:
       l = i.index("(")
       r= i.index(")")
       mul = i[l+1:r] #things between 
       muls = mul.split(",")
       if len(muls) != 2:
           return False
       for i in muls:
           if not i.isnumeric():
               return False
       else: 
           return muls

products1 = []
products2 = []
for i in data:
    muls = isvalid(i)
    if muls:
       p= int(muls[0]) * int(muls[1])
       products1.append(p)

items = []
a2 = a.split("don't()")
x = a2.pop(0)
items.append(x)
for n, i in enumerate(a2):
    if "do()" in i:
       z = i.split("do()")
       for g in z[1:]:
           items.append(g)
    else:
        a2[n+1] = a2[n] + a2[n + 1]

for l in items:
      data = l.split("mul")
      for i in data:
          muls = isvalid(i)
          if muls:
             p= int(muls[0]) * int(muls[1])
             products2.append(p)

print("part1: ", sum(products1))
print("part2: ", sum(products2))
f.close()