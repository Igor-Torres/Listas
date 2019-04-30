def tabela (x=32,y=128,z=5):
    print("+----------|-----|-----|-----+\n| binário  | oct | hex | chr |\n+----------|-----|-----|-----+")
    for j in range (x,y):
        q='{0:08b}'.format(j)
        a=q[:4]
        b=q[4:]
        print("|{1} {2} | {0:3o} | {0:3X} |  {0:1c}  |\n+----------|-----|-----|-----+".format(j,a,b))
        if (j-x)%z==0 and j-x!=0 and j!=y-1:
            print('\n+----------|-----|-----|-----+\n| binário  | oct | hex | chr |\n+----------|-----|-----|-----+')
        elif j==y-1:
           pass
 
