f = open("program.txt", "r")
str = f.read()
countColumn = str.count(";")
print(countColumn)
