def SeqFreq(n,S): #Finds the frequency numbers 1-9 follow n in sequence S
    i1=0
    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    i7=0
    i8=0
    i9=0
    for i in range(0,len(S)-1): #Does not check the last entry
        if S[i]==n:
            if S[i+1]==1: #Counts number of times 1 follows 4
                i1=i1+1
            if S[i+1]==2:
                i2=i2+1
            if S[i+1]==3:
                i3=i3+1
            if S[i+1]==4:
                i4=i4+1
            if S[i+1]==5:
                i5=i5+1
            if S[i+1]==6:
                i6=i6+1
            if S[i+1]==7:
                i7=i7+1
            if S[i+1]==8:
                i8=i8+1
            if S[i+1]==9:
                i9=i9+1
    print(n,' is followed by 1 ',i1,'times')
    print(n,' is followed by 2 ',i2,'times')
    print(n,' is followed by 3 ',i3,'times')
    print(n,' is followed by 4 ',i4,'times')
    print(n,' is followed by 5 ',i5,'times')
    print(n,' is followed by 6 ',i6,'times')
    print(n,' is followed by 7 ',i7,'times')
    print(n,' is followed by 8 ',i8,'times')
    print(n,' is followed by 9 ',i9,'times')
    
