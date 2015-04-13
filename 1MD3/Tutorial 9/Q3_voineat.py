def sortFile(src, dst):
    s = open(src, "r")
    toSort = s.readlines()
    toSort.sort()
    s.close()
    d = open(dst, "w")
    for i in toSort:
        print(i, file=d)
    d.close()
