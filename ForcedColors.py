def ForcedColors(w,k,coloring): #Use after BadColors3
    n=len(coloring)
    l=lvl(coloring) #the last lvl of current graph
    j=0
    while j>=0:
        j=j-1
        for i in range(1,n+1): #The verts of lvl l+1
            h=parent(i,w)
            if coloring[i-1]==0 and coloring[h-1]!=0:
                bad=BadColorsV(n,i,w,k,coloring)
                #print('bad colors of vertex i:',i,bad)
                if k-len(bad)<w: #added stuff everything above this works
                    print('Impossible to color')
                    return coloring
                if k-len(bad)==w: #colors the forced vertices
                    j=j+1
                    h=parent(i,w)
                    colors=[i for i in range(1,k+1)] #[1,2,...k]
                    goodcolors=RemoveCommon(colors,bad) #returns colors-badcolors
                    #print('The Good Colosr are:',goodcolors)
                    for m in range(0,w): #Finds the label of children of i
                        p=parent(i,w)
                        o=w*p+m #children of vertex p (parent of i)
                        coloring[o-1]=goodcolors[m]
    return coloring
