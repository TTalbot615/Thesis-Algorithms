def RandomTries3(x,k,color): #x number of tries
    y=0
    n=len(color)
    l=lvl(color)
    #BadColors4(2,k,color) #Not necessary if you've already run it (This colors the forced colors)
    c=changed(color)
    while y<x:
        print()
        print('Trial#:',y)
        RandomLVL2(k,color)
        print(color) 
        l=lvl(color)
        n=len(color)
        for i in range(0,len(c)):
            color[c[i]-1]=0
        y+=1
    print('n=',len(color))

#Should Run faster than 2 since it evaluates badcolors4 only once instead of
        #at every step.
