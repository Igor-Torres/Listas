'''Esta é uma função que calcula a soma dos algarismo de qualquer potência que não seja raíz
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''
def fun():    
    z=0
    p=[]
    print('Soma de todos os algarismos de uma potência (sem raíz):\n')
    q=int(input('defina a base da potencia: '))
    w=int(input('escolha o expoente da potencia:\n '))
    e=q**w
    u=tuple(str(e))
    for i in range(len(u)):
        z+=int(u[i])
    print('O resultado da sua potência é '+str(e)+', e a soma de seus algarismos é:\n ')
    p.append(z)
    print(p)

