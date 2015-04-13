import math
def geometric_mean(l):
	total = 1
	for i in l:
		total = total * i
	return(pow(total, (1/len(l))))
