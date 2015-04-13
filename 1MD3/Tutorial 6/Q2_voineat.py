#Q2

def daysInMonth(month, year):
  d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    d[1] = 29
  return d[month - 1]