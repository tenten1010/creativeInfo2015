def searchSame(i):

	if i+1 < len(lines) and lines[i+1] == lines[i]:
		return(searchSame(i+1))
	else:
		return(i)

def main(i):
	while i < len(lines):
		a = searchSame(i)
		if a - i >= 3:
			print(lines[i])
			i += a-i
		else:
			i +=1

if __name__ == '__main__':
	f = open("program.txt", "r")
	lines = f.readlines()
	main(0)
	
