class FileNotFoundError(Exception):
	pass
def sortbytime(src,dst):
	try:
		myFile = open(src, "r")
	except:
		raise FileNotFoundError()
	lines = myFile.readlines()
	for i in lines:
		i = i.split(',')
	print(lines)
	myFile.close()
	lines.sort()
	myFile = open(dst, "w")
	for i in lines:
		for j in i:
			j = j.replace('\n', "")
			print(j, file=myFile, end="")
		print("", file = myFile)
	myFile.close()
	return lines
def mergebytime(src1, src2, dst):
	lines  = sortbytime(src1, dst) + sortbytime(src2,dst)
	lines.sort()
	myFile = open(dst, "w")
	for i in lines:
		for j in i:
			print(j, file=myFile, end="")
		print("", file = myFile)
	myFile.close()