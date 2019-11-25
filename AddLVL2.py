def AddLVL(n,w,k,coloring):
    l=round(log2(n+1)-1) #level at start
    z=[0]*(2**(l+1)) #used to fill the end with zeroes
    coloring+=z
    for m in range(2**l,n+1):
        q=color(m,coloring)
        i=1
        repf=False
        while i<k+1 and repf==False:
            print(i,coloring)
            if i!=q:
                coloring[m*w-1]=i
                coloring[m*w]=i+1
                repf=RepFree(n,w,coloring)
                print('c',i,'=',coloring,m,'color of parent=',q,repf)
            i=i+1
            if i==k:
                print('failure')
    return coloring
