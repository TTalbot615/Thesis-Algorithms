def Que(k,Q,S): #Q=[[u,v,u,v,u,v,'left']] Checks if rep involving u and v
    rep=False #Not in a repetition together
    u=Q[0][0]
    v=Q[0][1]
    while Q!=[]:
        #print(Q)
        u1=Q[0][2]
        v1=Q[0][3]
        u2=Q[0][4]
        v2=Q[0][5]
        if S[u2]==S[v2]:
            #print('1')
            if v2==u2+k+1:
                rep=True
                print(u,v,u2,v2)
                return rep
            if v2<=u+k:
                rep=True
                print(u,v,u2,v2)
                return rep
            if Q[0][6]=='left':
                #print('3')
                if u1==u2+k-1: #Close enough to be a turn around, check both directions
                    if S[u2-1]==S[v2-1] and u2>0: #left
                        #print('a')
                        Q.append([u,v,u2,v2,u2-1,v2-1,'left'])
                    if S[u2-1]==S[v2-2] and u2>0: #left
                        #print('b')
                        Q.append([u,v,u2,v2,u2-1,v2-2,'left'])
                    if S[u2-2]==S[v2-1] and u2>0: #left
                        #print('c')
                        Q.append([u,v,u2,v2,u2-2,v2-1,'left'])
                    if S[u2-2]==S[v2-2] and u2>0: #left
                        #print('d')
                        Q.append([u,v,u2,v2,u2-2,v2-2,'left'])
                    if S[u2+1]==S[v2-1]: #right
                        #print('e')
                        Q.append([u,v,u2,v2,u2+1,v2-1,'right'])
                    if S[u2+1]==S[v2-2]: #right
                        #print('f')
                        Q.append([u,v,u2,v2,u2+1,v2-2,'right'])
                    if S[u2+2]==S[v2-1]: #right
                        #print('g')
                        Q.append([u,v,u2,v2,u2+2,v2-1,'right'])
                    if S[u2+2]==S[v2-2]: #right
                        #print('h')
                        Q.append([u,v,u2,v2,u2+2,v2-2,'right'])
                else: #Must keep moving to the left
                    if S[u2-1]==S[v2-1] and u2>0: #left
                        Q.append([u,v,u2,v2,u2-1,v2-1,'left'])
                    if S[u2-1]==S[v2-2] and u2>0: #left
                        Q.append([u,v,u2,v2,u2-1,v2-2,'left'])
                    if S[u2-2]==S[v2-1] and u2>0: #left
                        Q.append([u,v,u2,v2,u2-2,v2-1,'left'])
                    if S[u2-2]==S[v2-2] and u2>0: #left
                        Q.append([u,v,u2,v2,u2-2,v2-2,'left'])
            if Q[0][6]=='right': #Must keep moving right, check only the right
                #print('2')
                if S[u2+1]==S[v2-1]: #right
                    Q.append([u,v,u2,v2,u2+1,v2-1,'right'])
                if S[u2+1]==S[v2-2]: #right
                    Q.append([u,v,u2,v2,u2+1,v2-2,'right'])
                if S[u2+2]==S[v2-1]: #right
                    Q.append([u,v,u2,v2,u2+2,v2-1,'right'])
                if S[u2+2]==S[v2-2]: #right
                    Q.append([u,v,u2,v2,u2+2,v2-2,'right'])
        Q.pop(0)
        if Q==[]:
            return rep


#test line Que(2,[[2,10,2,10,2,10,'left']],[1,2,3,4,1,5,6,4,2,1,3])  Que(2,[[0,3,0,3,-4,3,'right']],[1,2,3,1])
