def isISBN(n):
	if not(len(n) == 10):
		return False
	else:
		c = list(n)
		if (c[len(c)-1] == 'X'):
			c[len(c)-1] = '10'
		c = list(map(int, c))
		checksum = 0

		for i in range(1,10):
			checksum += i* c[i-1]
		if ((checksum % 11) == c[9]):
			return True
		else: return False
def isISBNdash(n):
	if n.count('-') == 3 and n[1] == '-' and n[5] == '-' and n[11] == '-' and len(n) == 13 and isISBN("".join(n.split('-'))) == True:
		return True
	else:
		return False