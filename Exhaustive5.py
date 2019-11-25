def Exhaustive5(k,c,Q): #k-ary, c colors,Q seeds to try
    while Q!=[]:
        bad=[]
        Q1=[]
        q=Q[len(Q)-1] #last entry of Q
        colors=[i for i in range(1,c+1)] #Creates [1,2,...,c]
        for j in range(1,5): #Creates a list of the last 4 entries (bad colors) (Only line I changed from prev program)
            bad.append(Q[len(Q)-1][len(Q[len(Q)-1])-j])
        goodcolors=RemoveCommon(colors,bad) #List of the colors to try for extension
        for j in range(0,len(goodcolors)):
            q1=q+[goodcolors[j]]
            if SeqRep(k,q1)==False: #No repetition
                Q1.append(q1)
            if j==len(goodcolors)-1:
                if len(Q1)==0: #This entry is maximal and cannot extend
                    print('Maximal',q)
                    del Q[len(Q)-1]
                else:
                    del Q[len(Q)-1]
                    Q=Q+Q1 #Adds the new possiblities

#The goal is to have any subsequence of 5 consecutive entries be unique
                    #Ex: 13643 the next entries possible are 1,5 (using 6 colors)

#Spit out
#[1, 2, 3, 4, 5, 7, 6, 3, 4, 5, 2, 1, 7, 6, 5, 4, 3, 7, 6, 5, 2, 1, 7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 2, 1, 7, 4, 3, 6, 5, 7, 4, 3, 2, 1, 7, 6, 5, 4, 3, 7, 6, 5, 2, 1, 7, 6, 5, 4, 3, 7, 2, 1, 6, 5, 7, 2, 4, 3, 6, 7, 5, 1, 4, 3, 7, 6, 2, 4, 5, 7, 3, 1, 6, 5, 7, 4, 3, 2, 5, 7, 6, 4, 1, 5, 7, 6, 3, 2, 5, 4, 1, 7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 1, 7, 2, 5, 6, 3, 4, 2, 5, 1, 7, 6, 4, 5, 3, 2, 7, 6, 1, 4, 2, 5, 7, 6, 3, 2, 5, 7, 4, 1, 3, 5, 6, 7, 2, 3, 5, 6, 1, 4, 7, 5, 6, 3, 2, 7, 4, 6, 5, 1, 7, 4, 3, 6, 2, 7, 5, 4, 3, 1, 7, 6, 2, 4, 5, 7, 6, 3, 2, 1, 7, 6, 3, 5, 4, 7, 6, 1, 2, 5, 4, 7, 6, 3, 5, 4, 7, 2, 1, 6, 4, 7, 5, 3, 6, 2, 7, 4, 1, 6, 5, 7, 2, 3, 4, 5, 7, 6, 2, 1, 5, 7, 6, 4, 3, 5, 7, 1, 2, 6, 4, 7, 5, 3, 6, 4, 7, 2, 1, 3, 4, 7, 6, 5, 3, 2, 1, 7, 6, 5, 4, 3, 7, 6, 5, 1, 2, 4, 6, 7, 5, 3, 4, 6, 7, 2, 1, 5, 6, 7, 4, 3, 5, 2, 7, 6, 1, 5, 4, 7, 2, 3, 6, 4, 7, 5, 1, 3, 6, 2, 7]
                    #As one of the ones for c=7 (len is 292)


