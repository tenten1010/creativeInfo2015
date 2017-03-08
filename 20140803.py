f = open("program.txt", "r")
lines = f.readlines()
arr = []
for index,line in enumerate(lines):
	if line == lines[index-1]:
		if index+1<len(lines) and line == lines[index+1]:
			continue
		print(line)
