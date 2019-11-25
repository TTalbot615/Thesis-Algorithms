def LVLprinter(coloring):
    l=lvl(coloring)
    for i in range(0,l+1):
        s=(2**i)-1
        e=2**(i+1)-1
        print(noComma(coloring[s:e]))
