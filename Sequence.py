def Sequence(S): #Rep-free 3 symbol sequence
    m=len(S)
    A=[0]*(2*m)
    for i in range(0,2*m,2): #Replaces x with x,x' in S
        j=i//2
        A[i]=S[j]
    for i in range(1,2*m,2): #x'=x+4
        A[i]=4+A[i-1]
    for i in range(4,2*m,5): #Every 5th entry is a 4
        A.insert(i,4)
    A.append(4)#Adds a 4 to the very end
    return A
        
    
