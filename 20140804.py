f = open("program.txt", "r")
lines = f.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace("\n","")
lines = sorted(lines)
for i in range(len(lines)-1):
		j = i + 1
		count = 1
		while j < len(lines):
			if lines[j] != ".":
				if lines[j] == lines[i]:
					count += 1
					lines[j] = "."
			j += 1

		if count > 1:
			print("%s %d"%(lines[i],count))