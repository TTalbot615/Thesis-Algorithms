def PyramidOutput(coloring):
    #print('\n'.join([(10-i)*' '+(str(i)+' ')*i for i in range(1,10)]))
    l=lvl(coloring)
    for i in range(2,l+1):
        space=(80-2**i)*' '
        s=(2**i)-1
        e=2**(i+1)-1
        print(space,noComma(coloring[s:e]))
