from sys import argv as args
f = open(args[2], "r")
input = f.read().split(" ")

def blink(stones):
    newline = []
    for i in stones:
        if str(i) == "0":
            newline.append("1")
        elif len(str(i)) % 2 == 0:
            i = str(i)
            half = len(i) // 2
            two = int(i[half:])
            newline.append(str(i[:half]))
            newline.append(str(two))
        else:
            x = int(i) * 2024
            newline.append(str(x))
    return newline

if args[1] == "1":
		blinks = 25
		while blinks > 0:
			input = blink(input)
			blinks -= 1
		print(f"Part 1: {len(input)}")
else:
	raise NotImplementedError("Part 2 not implemented")
f.close()
