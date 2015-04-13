def bound(l):
	smallest = l[0]
	biggest = l[0]
	for i in l:
		if i > biggest:
			biggest = i
		if i < smallest:
			smallest = i
	return (smallest,biggest)