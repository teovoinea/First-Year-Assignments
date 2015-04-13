
def similarity(s,t):
    charsT = set()
    for i in t:
        charsT.add(i)
    charsS = set()
    for i in s:
        charsS.add(i)

    dictS = {}
    for i in charsS:
        dictS[i] = s.count(i)
    dictT = {}
    for i in charsT:
        dictT[i] = t.count(i)
    result = []
    for i in dictT:
        if i not in dictS or i not in dictT:
            continue
        smallest = min(dictT[i],dictS[i])
        biggest = max(dictT[i],dictS[i])
        difference = biggest - smallest
        if difference == 0:
            result.append(biggest)
        else:
            result.append(smallest)
    return sum(result)

def permutation(s,t):
    if len(s) != len(t):
        return False
    charsS = set()
    for i in s:
        charsS.add(i)
    charsT = set()
    for i in t:
        charsT.add(i)
    for i in charsT:
        if s.count(i) != t.count(i):
            return False
    for i in charsS:
        if s.count(i) != t.count(i):
            return False
    return True






