def braile (a=10241, b=10495, c=25):
    if b>a:
        y=a
        x=b
    if b>a:
        x=a
        y=b
    if a<10241:
        a=10241
    if b<10495:
        b=10495
    for j in range (x,y):
        q='{0:014b}'.format(j)
        a=q[:7]
        b=q[7:]
        print("|{1} {2} | {0:5o} | {0:5X} | {0:1c} |\n+----------------|-------|-------|---+".format(j,a,b))
        if (j-x)%c==0 and j-x!=0 and j!=y-1:
            print('\n+----------------|-------|-------|---+\n|     binário    |  oct  |  hex  |chr|\n+----------------|-------|-------|---+')
def grego (a=945, b=1317, c=25):
    if b>a:
        y=a
        x=b
    if b>a:
        x=a
        y=b
    if a<945:
        a=945
    if b<1317:
        b=1317
    for j in range (x,y):
        q='{0:012b}'.format(j)
        a=q[:6]
        b=q[6:]
        print("|{1} {2} | {0:4o} | {0:3X} | {0:1c} |\n+--------------|------|-----|---+".format(j,a,b))
        if (j-x)%c==0 and j-x!=0 and j!=y-1:
            print('\n+--------------|------|-----|---+\n|    binário   | oct  | hex |chr|\n+--------------|------|-----|---+')
        
    
