def tabela (x,y,z):
    print("+----------|-----|-----|-----+\n| binário  | oct | hex | chr |\n+----------|-----|-----|-----+")
    for j in range (x,y):
        print("| {0:8b} | {0:3o} | {0:3X} |  {0:1c}  |\n+----------|-----|-----|-----+".format(j))
        if (j-x)%z==0 and j-x!=0 and j!=y-1:
            print('\n+----------|-----|-----|-----+\n| binário  | oct | hex | chr |\n+----------|-----|-----|-----+')
        elif j==y-1:
           pass
 '''u='{0:8b}'.format(j)
    p=tuple(u)
    if len(p)<8:
        i=-1
        for t in len(p):
           i+=1
           k='0'+str(p[i])
           print(k) 
'''
 #séra q da certo isso de cima pra adicionar um zero ao binário?
