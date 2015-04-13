def shorten(s):
	vowels = ['a','e','i','o','u']
	chars = []
	for i in range(len(s)):
		if (s[i] not in vowels):
			chars.append(s[i])
	for i in range(len(chars)):
		print(chars[i], end = "")
	print()
def shortenPlus(s):
	vowels = ['a','e','i','o','u']
	print(s[0], end = "")
	for i in range(1,len(s), 1):
		if s[i - 1] == ' ' and s[i] in vowels:
			print(s[i], end = "")
		elif s[i] not in vowels:
			print(s[i], end = "")