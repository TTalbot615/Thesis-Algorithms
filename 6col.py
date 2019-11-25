def SixCol(l): #l is the lvl you want to build to
    col=[[1,2],[3,4],[5,6]]
    s=[-1,1,2,3,4,5,6]
    z=[0]*(2**(l+1)-len(s)-1)
    s+=z
    for v in range(4,2**(l)-1,2):
        l=lc(v,2)-1 #index of lc
        r=rc(v,2)-1
        ll=lc(v+1,2)-1 #index of lc of v+1
        rr=rc(v+1,2)-1
        print('v=',v)
        if color(v,s)==1:
            print('1')
            s[l]=3
            s[r]=4
            s[ll]=5
            s[rr]=6
            if RepFree(len(s),2,s)==False:
                print('1a')
                s[l]=5
                s[r]=6
                s[ll]=3
                s[rr]=4
                if RepFree(len(s),2,s)==False:
                    print('impossible')
        if color(v,s)==3:
            print('3')
            s[l]=1
            s[r]=2
            s[ll]=5
            s[rr]=6
            if RepFree(len(s),2,s)==False:
                print('3a')
                s[l]=5
                s[r]=6
                s[ll]=1
                s[rr]=2
                if RepFree(len(s),2,s)==False:
                    print('impossible')
        if color(v,s)==5:
            print('5')
            s[l]=3
            s[r]=4
            s[ll]=1
            s[rr]=2
            if RepFree(len(s),2,s)==False:
                print('5a')
                s[l]=1
                s[r]=2
                s[ll]=3
                s[rr]=4
                if RepFree(len(s),2,s)==False:
                    print('impossible')
    return s
