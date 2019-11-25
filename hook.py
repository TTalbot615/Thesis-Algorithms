def hooks(k,palinfree): #Palin-free and rep-free of length level+1, k colors. 
    l=len(palinfree)-1 #This is the number of levels
    n=2**(l+1)-1
    coloring=[0]*n #Initialize coloring to all 0's
    coloring[0]=-1 #colors the root
    print('Number of vertices',n,'Levels',l)
    for i in range(1,l+1): 
        coloring[(2**i)-1]=palinfree[i-1] #Places palinfree on the vertices 2,4,8,...2**l
        coloring[2**i]=palinfree[i] #Places plainfree on vertices 3,5,7,...2**l+1
    for j in range(3,l): #Avoid Grandchildren
        colors=[i for i in range(1,k+1)] #[1,2,...k]
        bad=[]
        bad.append(coloring[2**(j-2)-1]) # Color of Grandparent
        bad.append(coloring[2**(j-1)-1]) # Color of 
        bad.append(coloring[2**(j-1)]) #Color of parent
        good=RemoveCommon(colors,bad)
        coloring[2**j+1]=good[0]
        coloring[2**j+2]=good[1]
    for v in range(6,n+1): #Randomly color the remaining vertices if possible
        #print('vertex',v)
        coloring=ForcedColors(2,k,coloring)#Color the Forced Vertices
        if coloring[v-1]==0:
            badcol=BadColorsV(n,v,2,k,coloring)
            colorz=[i for i in range(1,k+1)] #[1,2,...k]
            goodcol=RemoveCommon(colorz,badcol)
            if len(goodcol)<2: #added stuff everything above this works
                print('Impossible to color')
                print('Cant color',v,'available colors',goodcol)
                return coloring
            if len(goodcol)>=2: #colors the forced vertices
                r=random.sample(goodcol,2)
                coloring[v-1]=r[0]
                coloring[v]=r[1]
    return coloring

#Hook rule and no grandchildren
