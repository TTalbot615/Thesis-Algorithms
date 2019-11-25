def BadColorsV(n,v,w,k,coloring): #Finds bad colors for vertex v, RUN FILL0 if needed on Coloring
    badcolors=[]
    p=parent(v,w)
    q=color(p,coloring)
    for j in range(1,k+1):
        if j==q: #don't do for the color of it's parent
            badcolors.append(j)
        else:
            coloring[v-1]=j
            if RepFree(n,w,coloring)==False:
                badcolors.append(j)
        coloring[v-1]=0
    return badcolors
