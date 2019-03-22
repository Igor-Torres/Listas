'''Esta função calcula as raízes de uma equação de grau dois.
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''
loop=0
while loop<10:
    
    print ('Equação do segundo grau')
    print ('')
    print('No formato ax²+bx+c (apenas raízes reais)')
    print ('')
    a=float(input("Defina o coeficiente 'a', que antecede x²:"))
    b=float(input("Defina o coeficiente 'b', que antecede x:"))
    c=float(input("Defina o coeficiente 'c', que é independente:"))
    if(a!=0):
        delta=(float(b**2 - 4*a*c))
    if(delta>0):
            print ('')
            print("Essas são as raízes reais da equação ("+str(a)+")x²+("+str(b)+")x+("+str(c)+"):")
            print(float(-b + (delta)**0.5)/(2*a))
            print(float(-b - (delta)**0.5)/(2*a))
            print('')
            print('')
    if(delta==0):
            print ('')
            print("Essa é a raiz única da equação ("+str(a)+")x²+("+str(b)+")x+("+str(c)+"):")
            print(float(-b + (delta)**0.5)/(2*a))
            print('')
            print('')
    if(delta<0):
            print ('')
            print("A equação ("+str(a)+")x²+("+str(b)+")x+("+str(c)+") não possui raízes reais.")
            print('')
            print('')

