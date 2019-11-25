def changed(color):
    n=len(color)
    l=lvl(color)
    change=[]
    for m in range(2**l,n+1): #vertices in the last level
        if color[m-1]==0:
            change.append(m)
    return change

#Keeps track of all entires that are zero so they can be changed back so the program can loop
