
'''O programa serve para calcular quais postos N estao no raio de X km
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''
b=[]
c=[]
print('Ache os postos no raio de X km')
print('')
print('')
n=int(input('Defina o número de postos: '))
print('')
a=float(input('Escolha em qual raio você deseja achar quais dos '+str(n)+' postos estão contidos: '))
print('')
coordenada1=float(input('Defina sua coordenada x: '))
coordenada2=float(input('Defina sua coordenada y: '))
print('')
print('')
for i in range(n):
        if i!=(n):
                i+=1
                x=float(input('Defina a coordenada x do seu posto número '+str(i)+' : '))
                y=float(input('Defina a coordenada y do seu posto número '+str(i)+' : '))
                distância=((x-coordenada1)**2+(y-coordenada2)**2)**0.5       
                if distância<a:
                       c.append('('+str(x)+','+str(y)+')')
                       u= len(c)
print('')
print('Existem '+str(u)+' postos no raio de '+str(a)+' km; ') 
print('Essas são as coordenadas dos '+str(u)+' postos que estão neste raio: ')
print('')
print(c)
        


