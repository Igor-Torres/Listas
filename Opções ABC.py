'''Esta função cria um menu de opções em loop, incluindo operações vetoriais e a opção 'sair do programa'
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''
def calc():
  q=0
  s=[]
  while q<1:#para criar o loop e o menu sempre aparecer ao final de cada opção
      print('Opções:\n')
      print('1) Soma de dois vetores W=Y+U')
      print('2) Subtração de dois vetores W=Y-U')
      print('3) Sair do programa\n')
      o=int(input('Escolha a sua opção: '))
      print('')
      if o==1:
          vetor_1=[]
          vetor_2=[]
          soma_vetorial=[]
          print('')
          n=int(input('Defina as N dimensões do seu vetor Y e U: '))
          print('')
          for i in range(n):
            if i!=n:# loop 'for' criado para N dimensões
              i+=1
              x=float(input('Defina a coordenada do seu vetor Y na '+str(i)+'ª dimesão (caso o vetor não chegue até esta dimensão digite 0): '))
              y=float(input('Defina a coordenada do seu vetor U na '+str(i)+'ª dimesão (caso o vetor não chegue até esta dimensão digite 0): '))
              t=x+y
              vetor_1.append(x)#estética
              vetor_2.append(y)#estética
              soma_vetorial.append(t)#soma vetorial acrescentada a uma lista vazia
            if i==n:
              print('')
              print('Essa é a soma dos vetores '+str(vetor_1)+' e '+str(vetor_2)+' nas '+str(n)+' dimensões: ')
              print(soma_vetorial)
              print('')
              break
      if o==2:
        vetor_1=[]
        vetor_2=[]
        subtração_vetorial=[]
        print('')
        n=int(input('Defina as N dimensões do seu vetor Y e U: '))
        print('')
        for i in range(n):
            if i!=n:# loop 'for' criado para N dimensões
                i+=1
                x=float(input('Defina a coordenada do seu vetor Y na '+str(i)+'ª dimesão (caso o vetor não chegue até esta dimensão digite 0): '))
                y=float(input('Defina a coordenada do seu vetor U na '+str(i)+'ª dimesão (caso o vetor não chegue até esta dimensão digite 0): '))
                t=x-y
                vetor_1.append(x)#estética
                vetor_2.append(y)#estética
                subtração_vetorial.append(t)#soma vetorial acrescentada a uma lista vazia
            if i==n:    
              print('')
              print('Essa é a subtração dos vetores '+str(vetor_1)+' e '+str(vetor_2)+' nas '+str(n)+' dimensões: ')
              print(subtração_vetorial)
              print('')
              break
      if o==3:
        print('Programa encerrado.')
        break                
      if o>3:
          print('opção invalida')
          print('')
              
              
