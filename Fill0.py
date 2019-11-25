def Fill0(coloring):
    n=len(coloring)
    l=int(log2(n+1)-1) #the last lvl of current graph
    z=[0]*(2**(l+1))
    coloring+=z
    return coloring
