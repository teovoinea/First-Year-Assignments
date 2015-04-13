def median(l):
	result = 0
	if len(l) % 2 == 0:
		x1 = int(len(l) /2)
		result = (l[x1] + l[x1 - 1]) / 2
	elif len(l) == 1:
		result = l[0]
	else:
		result = l[int(len(l) / 2) + 1]
	return result