'''Esta é uma função que calcula os N primeiros múltiplos em comum de x,y.
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''

print('Calcule os N primeiros múltiplos em comum de (x,y) inteiros, além do 0.')
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
                a=x*j
                b=x*k#múltiplos 
                z.append(a)
                v.append(b)
print('') 
print('Os '+str(n)+' primeiros múltiplos de '+str(j)+' ,além do 0, são: ')
print(z)
print('')
print('Os '+str(n)+' primeiros múltiplos de '+str(k)+' ,além do 0, são: ')
print(v)
m=0
n=0
f=len(z)
g=len(v)
for x in range (f):
        n+=z[x]#somamos os N primeiros múltiplos comuns
for y in range (g):
        m+=v[y]#somamos os N primeiros múltiplos comuns
a=m+n
print('')
print('A soma de todos os '+str(n)+' primeiros múltiplos de '+str(k)+' e '+str(j)+' é: ')
print(a)
