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
                a=x*k*j#múltiplos em comum
                z.append(a)
print('') 
print('Os '+str(n)+' primeiros múltiplos em comum de '+str(k)+' e '+str(j)+' ,além do 0, são: ')
print(z)
a=0
f=len(z)
for x in range (f):
        a+=z[x]#somamos os N primeiros múltiplos comuns
print('')
print('A soma de todos os '+str(n)+' primeiros múltiplos de '+str(k)+' e '+str(j)+' é: ')
print(a)
