'''Esta função cria um meno de opções em loop, incluindo operações vetoriais e a opção 'sair do programa'
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''
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
        a=float(input('Defina a sua coordenada X do primeiro vetor que deseja somar: '))
        b=float(input('Defina a sua coordenada Y do primeiro vetor que deseja somar: '))
        c=float(input('Defina a sua coordenada X do segundo vetor que deseja somar: '))
        d=float(input('Defina a sua coordenada Y do segundo vetor que deseja somar: '))
        somaX= a+c
        somaY= b+d
        s.append(''+str(somaX)+','+str(somaY)+'')
        print('Esta é a soma de seus vetores: ')
        print('')
        print(s)
        print('')
        s=[]#redefinimos S como vazio para o caso do usuário escolher outra conta, ou a mesma com outros vetores
    if o==2:
        a=float(input('Defina a sua coordenada X do primeiro vetor que deseja subtrair: '))     
        b=float(input('Defina a sua coordenada Y do primeiro vetor que deseja subtrair: '))
        c=float(input('Defina a sua coordenada X do segundo vetor que deseja subtrair: '))
        d=float(input('Defina a sua coordenada Y do segundo vetor que deseja subtrair: '))
        subtraçãoX= a-c
        subtraçãoY= b-d
        s.append(''+str(subtraçãoX)+','+str(subtraçãoY)+'')
        print('Esta é a subtração de seus vetores: ')
        print('')      
        print(s)
        print('')
        s=[]
    if o==3:
        print('Programa encerrado.')
        break                
    if o>3:
        print('opção invalida')
        print('')
              
              
