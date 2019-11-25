def BadColors4(w,k,coloring): #Same as 3 just doesn't print things
    n=len(coloring)
    l=int(log2(n+1)-1) #the last lvl of current graph
    z=[0]*(2**(l+1))
    coloring+=z
    y=len(coloring)
    x=2**(l+2)-1
    for i in range(n+1, 2**(l+2)): #The verts of lvl l+1
        bad=BadColorsV(y,i,w,k,coloring)
        #print('bad colors of vertex i:',i,bad)
        if k-len(bad)<w: #added stuff everything above this works
            print('Impossible to color')
            l=False
            return l
        if k-len(bad)==w: #colors the forced vertices
            h=parent(i,w)
            colors=[i for i in range(1,k+1)] #[1,2,...k]
            goodcolors=RemoveCommon(colors,bad) #returns colors-badcolors
            #print('The Good Colosr are:',goodcolors)
            for m in range(0,w): #Finds the label of children of i
                p=parent(i,w)
                o=w*p+m #children of vertex p (parent of i)
                coloring[o-1]=goodcolors[m]
    return coloring
