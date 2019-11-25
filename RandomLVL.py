def RandomLVL(k,coloring): #adds a random lvl to coloring
    import random
    n=len(coloring)
    l=round(log2(n+1)-1) #number of lvls in the graph currently
    z=[0]*(2**(l+1))
    coloring+=z
    for m in range(2**l,2**(l+1)): #colors the children of vertices in last lvl
        kcolor=[i for i in range(1,k+1)]
        left=lc(m,2)
        right=rc(m,2)
        bad=BadColorsV(len(coloring),left,2,k,coloring)
        i=RemoveCommon(kcolor,bad) #Colors to use on the children of m
        if len(i)<2:
            print('impossible to color vertex',left,right)
            return coloring
        j=random.sample(i,2)
        coloring[left-1]=j[0]
        coloring[right-1]=j[1]
        if m==2**(l+1)-1:
            n=len(coloring)
            l=round(log2(n+1)-1)
            print(coloring)
            print('The number of vertices is',n,'The level is',l)
            
    
