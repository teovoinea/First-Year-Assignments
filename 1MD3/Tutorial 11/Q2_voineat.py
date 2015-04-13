from random import *
def sortinghat(incoming, house):
	gryffindor = ["courage", "chivalry", "determination"]
	hufflepuff = ["valuing hard work", "patience", "loyalty", "fair play"]
	ravenclaw = ["witty", "ability to learn", "wisdom"]
	slytherin = ["pure-blood", "cunning", "resourcefulness", "ambition"]
	myFile = open(incoming, "r")
	lines = myFile.readlines()
	students = []
	for i in lines:
		students.append(i.split(','))
	myFile.close()
	myFile = open(house, "w")
	for i in students:
		gCount = 0
		hCount = 0
		rCount = 0
		sCount = 0
		for j in i:
			if j in gryffindor:
				gCount += 1
			if j in hufflepuff:
				hCount += 1
			if j in ravenclaw:
				rCount += 1
			if j in slytherin:
				sCount += 1
		houses = [gCount, hCount, rCount, sCount]
		b = [a for a, x in enumerate(houses) if x == max(houses)]
		if len(b) != 1:
			c = randint(0, len(b) - 1)
			d = b[c]
		else: d = b[0]
		if d == 0:
			print(i[0], ",Gryffindor", file = myFile)
		if d == 1:
			print(i[0], ",Hufflepuff", file = myFile)
		if d == 2:
			print(i[0], ",Ravenclaw", file = myFile)
		if d == 3:
			print(i[0], ",Slytherin", file = myFile)
