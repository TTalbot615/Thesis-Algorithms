def index(n): 
    B=[-1,0,1] #Index array
    C=[0]*(n-3)
    B+=C
    print(len(B))
    for i in range(3,n,2): #Edge above has index i, children are i+1,i+2 
        h=parent(i,2)
        B[i]=1+B[h]
        B[i+1]=1+B[i]
    return B
