#Q5

def longestAlphabeticalSubstring(s):
  sub =["",""]
  previous = 0
  longest = 0
  for i in range(len(s) - 1):
    if s[i] > s[i+1]:
      sub = sub + [s[previous:i+1]]
      previous = i+1
    elif i == len(s) - 2 and sub == ["",""]:
      sub = [s]
  for i in sub:
    if len(i) > longest:
      longest = len(i)
  for i in sub:
    if len(i) == longest:
      return i
      break
