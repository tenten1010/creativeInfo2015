def isSimilar(arr):
	difference = 0
	for i in range(len(arr[0])):
		if arr[0][i] != arr[1][i]:
			difference += 1
		else:
			continue
	if difference <= 5 and difference > 0:
		return True
	else:
		return False

def compare(a,b):
	length = []
	arr = []
	length.append(len(lines[a]))
	length.append(len(lines[b]))
	if min(length)> 20:
		arr.append(lines[a])
		arr.append(lines[b])
		arr[length.index(min(length))] += " "*(max(length)-min(length))
		if isSimilar(arr):
			print("%s\n%s\n\n"%(arr[0],arr[1]))

if __name__ == '__main__':
	f = open("program.txt", "r")
	lines = f.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].replace("\n","")
	for i in range(len(lines)-1):
		j = i + 1
		while j < len(lines):
			compare(i,j)
			j += 1