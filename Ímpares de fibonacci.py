'''Esta função calcula as somas dos termos ímpares em uma seqência de Fibonacci
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''
L=[0,1]#0 e 1 para conseguirmos iniciar uma soma dos termos anteriores
H=[]
n=0#para o loop while
valor=int(input('Defina o limite maximo para o valor do último termo da sequência: '))
print('')
a=0#para fazer a soma dos termos anteriores
while n<10:
        i=L[a]+L[a+1]
        a+=1
        if i>valor:
                break 
        else:
                L.append(i)#criando Fibonacci
q=len(L)
for y in range(q):
        if L[y]%2==0:
                pass#eliminando os números pares da lista
        else:
           H.append(L[y])
r=len(H)
print('Construindo uma sequência de Fibonacci, tendo o último elemento desta lista menor que '
+str(valor)+', teremos:')
print(L)
print('')
print('Agora separando os ímpares desta lista teremos: ')
print(H)
print('')
print('A soma de todos os elementos desta lista é:')
w=0#para a soma dos termos da lista definimos esta variável
if r!=0:
        for x in range(r):                
                e=H[x]
                w+=e
print(w)
        
