def proper(coloring): #Only for w=2 for now
    n=len(coloring)
    proper=True
    l=lvl(coloring)
    m=2**l-1
    for v in range(2,n,2):
        u=parent(v,2)
        w=rc(u,2)
        #print('v',v,'has parent',u,'with right child',w)
        if color(v,coloring)==color(u,coloring):
            print(v,'Same Color as parent',u)
            proper=False
        if color(v,coloring)==color(w,coloring):
            print(v,'Same Color as other child',w)
            proper=False
    return proper
                                    
#Might Work, probably does
