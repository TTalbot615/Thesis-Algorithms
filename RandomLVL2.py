def RandomLVL2(k,coloring): #adds a random lvl to a coloring where Bad3 has run
    import random
    n=len(coloring)
    l=lvl(coloring) #number of lvls in the graph currently
    for m in range(2**l,n+1): #colors the children of vertices in last lvl
        if coloring[m-1]==0: #if the color was not forced color this vertex
            kcolor=[i for i in range(1,k+1)]
            o=parent(m,2)
            left=lc(o,2)
            right=rc(o,2)
            bad=BadColorsV(len(coloring),left,2,k,coloring)
            i=RemoveCommon(kcolor,bad) #Colors to use on the children of o
            if len(i)<2:
                print('impossible coloring below, cannot color',left)
                return coloring
            else:
                j=random.sample(i,2)
                coloring[left-1]=j[0]
                coloring[right-1]=j[1]
    return coloring

#works
