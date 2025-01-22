from sys import argv as args
f = open(args[2], "r")
file = f.read()

if args[1] == "1":
		block= []
		idnum = 0
		for n,i in enumerate(file):
			if n % 2 == 0 or n == 0:
				id = idnum
				idnum += 1
				for i in range(int(i)):
				  block.append(id)
			else:
				for i in range(int(i)):
				  block.append(".")

		rev = list(reversed(block))

		c = block.count(".")
		for n, i in enumerate(rev):
			if i != ".":
				if '.' in block:
				  idx = block.index('.')
				  block[idx] = i

		sorted = block[:-c]
		prods = []   
		for n, i in enumerate(sorted):
			if i != ".":
			  x = i * n
			  prods.append(x)

		print("pt1: ",sum(prods))
else:
	raise NotImplementedError("Part 2 was not implemented")
f.close()
