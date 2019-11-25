def RandomTries(x,k,color): #x is the number of times to try and find a coloring that works
    col=False
    y=0
    while y<x+1:
        #print(y)
        RandomLVL(k,color)
        #print(color)
        #BadColors4(2,k,color) #Adds to many zeroes
        print(color)
        l=lvl(color)
        n=len(color)
        color[2**l-1:n]=[]
        #print(color)
        y+=1
        
        
        


#Doesn't work yet, for some reason it's changing coloring
        #The problem is that when you run Random it changes color as it runs
        #it doesn't keep the initial value saved, and setting things equal changes both
