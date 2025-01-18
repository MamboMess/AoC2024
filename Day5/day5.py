
f = open("input.txt", "r")
data = f.read().split("\n\n")
d1 = data[0].split("\n")
d2 = data[1].split("\n")
r = [d.split("|") for d in d1]
updates = [d.split(",") for d in d2]

rules = {}
for [x,y] in r:
    if x not in rules:
        rules[x] = []
        rules[x].append(y)
    else:
        rules[x].append(y)

correct = []
incorrect = []

def get(ls):
    m = len(ls)/2
    return ls[int(m)]
    
def check(ls):
    for n,p in enumerate(ls):
        if p in rules:
            prules= rules[p] #this page (p) must come before all the pages in prules, so check if any of these numbers show up before it 
            nums = ls[:n] #pages before current page
            for pr in prules:
                if pr in nums:
                    return False
    return True 
                                                         
def shuffle(ls):
    dict = {}
    newls = []
    for n,p in enumerate(ls):
        dict[p] = n
        if p not in rules:
            pass
        elif n != 0:
            prules = rules[p]
            nums = ls[:n]
            for x, i in enumerate(nums):
                if i in prules and x < dict[p]:
                    dict[p] = x
    for k in dict:
       newls.insert(dict[k], k)
    return newls

for ls in updates: #pt1
    if check(ls):
        correct.append(int(get(ls)))
    else:
       incorrect.append(ls)
print("pt1: ", sum(correct))    

#pt2                        
corrected=[]
while len(incorrect) != 0:
    ls = incorrect.pop(0)
    while not check(ls):
        ls = shuffle(ls)
    corrected.append(int(get(ls)))
print("pt2: ", sum(corrected))

f.close()