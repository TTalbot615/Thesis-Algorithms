#My first attempt at the hook rule, does not work.

def hooks(k,palin): #Creates a coloring using the hook idea (start palindrome with 1)
    l=len(palin) #This is the number of levels
    n=2**(l+1)-1
    coloring=[0]*n #Initialize coloring to all 0's
    for i in range(1,l+1): #Places the palindrome on the vertices 2,4,8,...2**l
        coloring[(2**i)-1]=palin[i-1]
    coloring[0]=-1 #colors the root
    for j in range(1,l):#right children forced by hook rule
        coloring[2**j]=palin[j]
    u=(2**l)+1 #Needs special attention, everything else will get done in pairs
    y=goodcolors(u,k,coloring)
    a=random.randint(1,len(y))
    coloring[u-1]=y[a-1] #Color this specially so the next loop works
    print(coloring)
    for q in range(6,n+1): #Color top to bottom, left to right (note 1-5 are already colored)
        if coloring[q-1]==0:
            p=parent(q,2)
            good=goodcolors(q,k,coloring)
            r=rc(p,2) #Right child
            if len(good)>1:
                z=random.sample(good,2) #Color in pairs
                print('random colors to assign',z,'q and r',q,r)
                coloring[q-1]=z[0]
                coloring[r-1]=z[1]
                s=lc(q,2) #left child of q
                if q<2**l:
                    coloring[s-1]=color(r,coloring) #forced by the hook rule
                    t=rc(q,2)
                    y=goodcolors(t,k,coloring)
                    if len(y)>0:
                        a=random.randint(1,len(y))
                        coloring[t-1]=y[a-1]
                    else:
                        print('cant color hook neighbor',t)
                        return coloring
            else:
                print('Not enough good colors,cant color q',q,'and r',r)
            print(coloring)
    return coloring

#Not entirely sure it works. Freaks out for 5,[1,2,3,4,5,2] says it can't do it. Will not accept [1,2,3,4,5,3] see why
        
