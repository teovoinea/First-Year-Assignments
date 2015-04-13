def occurrences( s : "string", t : "substring"):
	if len(s) < len(t):
		return 0
	else:
		counter = 0
		for i in range(len(s)):
			if i + len(t) > len(s):
				break
			elif s[i:i+len(t)] == t:
				counter = counter + 1
		return counter