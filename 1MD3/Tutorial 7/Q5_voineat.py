def one_mode(l):
	unique = set(l)
	most = 0
	indexMost = 0
	for i in unique:
		if l.count(i) > most:
			most = l.count(i)
	mode = 0
	for i in l:
		if l.count(i) == most:
			mode = i
	return (mode, most)

def all_modes(l):
	unique = set(l)
	most = 0
	for i in unique:
		if l.count(i) > most:
			most = l.count(i)
	modes = []
	for i in unique:
		if l.count(i) == most:
			modes.append(i)
	return(modes, most)
