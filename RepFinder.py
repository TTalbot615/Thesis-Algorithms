def RepFinder(u,v,w,coloring): #u>v are the verts rep occurs at with coloring
    repi=[]
    c=color(u,coloring)
    repi.append(c)
    while parent(u,w)>v: #They may not be related, there could be a turning point, stops before this happens
        u=parent(u,w)
        c=color(u,coloring)
        repi.append(c)
        print(repi,'u',u,'color of u',c)
    d=color(v,coloring)
    repi.append(d)
    return repi 

#First 1/2 of the repetition only, may be a little too long at the end, roughly works
        #Works well enough
