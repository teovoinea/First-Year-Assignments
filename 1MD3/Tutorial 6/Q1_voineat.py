#Q1
def area(p):
  total = 0
  for i in range(len(p) - 1):
    total = total + (p[i][0]*p[i+1][1] - p[i+1][0]*p[i][1])
  return total * 0.5