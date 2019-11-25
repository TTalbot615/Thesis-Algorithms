def RemoveCommon(a, b): #returns a-(a intersect b)
    for e in a[:]:
        if e in b:
            a.remove(e)
            b.remove(e)
    return a
