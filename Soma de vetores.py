'''Função para calcular a soma de vetores x,y em N dimensões
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''
vetor_1=[]
vetor_2=[]
soma_vetorial=[]
print('Função para somar vetores x e y em N dimensões')
print('')
n=int(input('Defina as N dimensões do seu vetor A e B: '))
print('')
for i in range(n):
    if i!=n:# loop 'for' criado para N dimensões
        i+=1
        x=float(input('Defina a coordenada do seu vetor A na '+str(i)+'ª dimesão (caso o vetor não chegue até esta dimensão digite 0): '))
        y=float(input('Defina a coordenada do seu vetor B na '+str(i)+'ª dimesão (caso o vetor não chegue até esta dimensão digite 0): '))
        t=x+y
        vetor_1.append(x)#estética
        vetor_2.append(y)#estética
        soma_vetorial.append(t)#soma vetorial acrescentada a uma lista vazia
    if i==n:    
       break
print('')
print('Essa é a soma dos vetores '+str(vetor_1)+' e '+str(vetor_2)+' nas '+str(n)+' dimensões: ')
print(soma_vetorial)

