def SequenceColoring(S): #len(S) should be 2**l
    l=len(S)//2
    n=2**(l+1)-1
    Seq=Sequence(S) #Replaces x with x,x' and every 5th entry is 4
    coloring=[-1]*(n)
    D=index(n) #Index Array
    for i in range(1,n):
        coloring[i]=Seq[D[i]]
    return coloring,RepFree(n,2,coloring)
