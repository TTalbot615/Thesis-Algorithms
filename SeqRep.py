def SeqRep(k,S):
    print('False means rep free')
    for i in range(0,len(S)):
        for j in range(0,len(S)):
            if j>i+k:
                if Que(k,[[i,j,i,j,i,j,'left']],S)==True:
                    rep=True
                    return rep,'there is a repetition'
                else:
                    rep=False
    return rep
