def Exhaustive(k,c): #k-ary, c colors
    Q=[[1,2,3,4,]]
    while Q!=[]:
        bad=[]
        colors=[i for i in range(1,c+1)]
        for j in range(1,k+2): #Creates a list of the last k+1 entries of current seq
            bad.append(Q[len(Q)-1][len(Q[len(Q)-1])-j])
        goodcolors=RemoveCommon(colors,bad) #List of the colors to try for extension
        for j in range (0,len(goodcolors)):
            Q[len(Q-1)].append(goodcolors[j])



#Goal is to print an exhaustive list of rep free seq for the given number of colors
