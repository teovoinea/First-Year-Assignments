#Q4

def grayCode(width):
  if width == 1:
    return [0,1]
  else:
    first = grayCode(width - 1)
    second = first[::-1]
    for i in range(len(first)):
      first[i] = [0] + [first[i]]
    for i in range(len(second)):
      second[i] = [1] + [second[i]]
    total =  first + second
    return total
