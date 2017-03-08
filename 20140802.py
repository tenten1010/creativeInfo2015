f = open("program.txt", "r")
lines = f.readlines()

for index,line in enumerate(lines):
	print("%d "%index+line)