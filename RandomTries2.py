def RandomTries2(x,k,color): #x number of tries
    y=0
    n=len(color)
    l=lvl(color)
    while y<x:
        print()
        print(y)
        BadColors4(2,k,color) #4 just doesn't print as much as 3
        RandomLVL2(k,color)
        print(color) 
        l=lvl(color)
        n=len(color)
        color[2**l-1:n]=[]
        y+=1

