from random import *
from graphics import *
win = GraphWin("Maze",600, 600)
win.setBackground("white")
class MyStack():
	def __init__(self, starting=[]):
		assert type(starting) == type([])
		self.S = starting
	def __str__(self):
		returnArray = []
		for i in self.S:
			returnArray.append(str(i))
		return str(returnArray)
	def push(self, item):
		self.S.append(item)
	def pop(self):
		return self.S.pop(len(self.S) - 1)
	def isEmpty(self):
		if not self.S:
			return True
		else:
			return False
	def size(S):
		return len(self.S)
class Cell():
	def __init__(self, x, y, isStart=False, isEnd = False, visited=False):
		self.x = x
		self.y = y
		self.visited = visited
		self.north = True
		self.south = True
		self.east = True
		self.west = True
		self.path = False

	def North(self, factor):
		line = Line(Point(self.x*(factor) + 2, self.y*factor + 2), Point(self.x*factor + factor + 2, self.y*factor + 2))
		if self.north:
			line.setFill("black")
		else:
			line.setFill("white")
		line.draw(win)
	def South(self, factor):
		line = Line(Point(self.x*(factor) + 2, self.y*factor + 2), Point(self.x*factor + factor + 2, self.y*factor + 2))
		if self.south:
			line.setFill("black")
		else:
			line.setFill("white")
		line.draw(win)
	def East(self, factor):
		line = Line(Point(self.x*(factor) + 2, self.y*factor + 2), Point(self.x*factor + 2, self.y*factor + factor + 2))
		if self.east:
			line.setFill("black")
		else:
			line.setFill("white")
		line.draw(win)
	def West(self, factor):
		line = Line(Point(self.x*(factor) + 2, self.y*factor + 2), Point(self.x*factor + 2, self.y*factor + factor + 2))
		if self.west:
			line.setFill("black")
		else:
			line.setFill("white")
		line.draw(win)

	def Path(self, factor):
		if self.path:
			corner1 = Point(self.x*factor + 2, self.y*factor + 2)
			corner2 = Point(self.x*factor + factor + 2, self.y*factor + factor + 2)
			rect = Rectangle(corner1, corner2)
			rect.setFill("yellow")
			rect.draw(win)


	def allWalls(self):
		if self.north and self.south and self.east and self.west:
			return True
		else:
			return False
	def DrawCells(self, factor):
		
		self.North(factor)
		self.South(factor)
		self.East(factor)
		self.West(factor)
		self.Path(factor)

	def __str__(self):
		return "".join(["[", str(self.x), ", ", str(self.y), "] "])
class Maze():
	def __init__(self, n):
		self.M = []
		self.n = n
		self.M = [[Cell(i,j, True) for i in range(n)]for j in range(n)]
		self.M[0][0] = Cell(0, 0, True)
		self.M[n - 1][n - 1] = Cell(n - 1, n - 1, False, False)
		rect = Rectangle(Point(2,2), Point(502, 502))
		rect.draw(win)
	def draw(self):
		for i in range(0, len(self.M), 1):
			for j in range(0, len(self.M), 1):
				self.M[i][j].DrawCells(500/self.n)
					
	def __str__(self):
		returnList = []
		for i in range(len(self.M)):
			for j in range(len(self.M)):
				returnList.append(str(self.M[i][j]))
				print(str(self.M[i][j]))
		returnString = [i for i in returnList]
		return str(returnString)	

	def explore(x,y):
		self.M[x][y].isVisited = True
		print(str(self.M[x][y]))
		if y + 1 <= 8 and not self.M[x][y+1].isVisited:
			explore(x, y+1)
		if x + 1 <= 8 and not self.M[x+1][y].isVisited:
			explore(x+1,y)
		if y - 1 >= 0 and not self.M[x][y-1].isVisited:
			explore(x,y-1)
		if x - 1 >= 0 and not self.M[x-1][y].isVisited:
			explore(x-1,y)

	def knockWalls(self):
		x = randint(0,self.n - 1)
		y = randint(0,self.n - 1)
		#print(self)
		stack = MyStack([])
		#print(self)
		totalCells = self.n * self.n
		#print(totalCells)
		visitedCells = 1
		self.M[x][y].visited = True
		currentCell = self.M[x][y]
		#print(self)
		stack.push(currentCell)
		#print(self.M[x][y])
		#print(self)
		allVisited = True
		while allVisited:
			goodNeighbours = []
			x = currentCell.x
			y = currentCell.y
			if x + 1 <= self.n - 1 and not self.M[x+1][y].visited:
				goodNeighbours.append(True)
			else: goodNeighbours.append(False)
			if x - 1 >= 0 and not self.M[x-1][y].visited:
				goodNeighbours.append(True)
			else: goodNeighbours.append(False)
			if y + 1 <= self.n - 1 and not self.M[x][y+1].visited:
				goodNeighbours.append(True)
			else: goodNeighbours.append(False)
			if y - 1 >= 0 and not self.M[x][y-1].visited:
				goodNeighbours.append(True)
			else: goodNeighbours.append(False)
			if True in goodNeighbours:
				xthTrue = randint(0, goodNeighbours.count(True))
				#print("Pre if, xth True: ", xthTrue)
				trueCount = 0
				for i in range(len(goodNeighbours)):
					if goodNeighbours[i]:
						if trueCount == xthTrue:
							#print("True count: ", trueCount)
							#print("#th true: ", xthTrue)
							#print("Good neighbours True count: ", goodNeighbours.count(True))
							#print(goodNeighbours)
							if i == 0:
								self.M[x][y].north = False
								self.M[x+1][y].south = False
								self.M[x+1][y].visited = True
								stack.push(currentCell)
								currentCell = self.M[x+1][y]
								#self.draw()
							if i == 1:
								self.M[x][y].south = False
								self.M[x-1][y].north = False
								self.M[x-1][y].visited = True
								stack.push(currentCell)
								currentCell = self.M[x-1][y]
								#self.draw()
							if i == 2:
								self.M[x][y].east = False
								self.M[x][y+1].west = False
								self.M[x][y+1].visited = True
								stack.push(currentCell)
								currentCell = self.M[x][y+1]
								#self.draw()
							if i == 3:
								self.M[x][y].west = False
								self.M[x][y-1].east = False
								self.M[x][y-1].visited = True
								stack.push(currentCell)
								currentCell = self.M[x][y-1]
								#self.draw()
						trueCount += 1
				visitedCells += 1
				#print(visitedCells)
			else:
				currentCell = stack.pop()
			visitedStatus = []
			for k in range(len(self.M)):
				for l in range(len(self.M)):
					visitedStatus.append(self.M[k][l].visited)
			#print(visitedStatus)					
			if False not in visitedStatus:
				allVisited = False	
