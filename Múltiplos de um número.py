'''Esta é uma função que calcula os N primeiros múltiplos de x,y.
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''

print('Calcule os N primeiros múltiplos de (x,y) inteiros, além do 0.')
print('')
z=[]
v=[]
k=int(input('Defina o primeiro número x que deseja calcular os N primeiros múltiplos:'))
print('')
j=int(input('Defina o segundo número y que deseja calcular os N primeiros múltiplos:'))
print('')
n=int(input('Defina o número N de múltiplos que deseja calcular: '))
for x in range(n+1):
        if x==0:
                pass
        if x!=0:
                a=x*k
                z.append(a)
                b=x*j
                v.append(b)
print('') 
print('Os '+str(n)+' primeiros múltiplos de '+str(k)+' ,além do 0, são: ')
print(z)
print('')
print('')
print('Os '+str(n)+' primeiros múltiplos de '+str(j)+' ,além do 0, são: ')
print(v)

      
