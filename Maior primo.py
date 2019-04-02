'''Achar o maior fator primo de um número
   Aluno: Igor Torres da Costa
   DRE: 119034669
   Curso: Matemática Aplicada
   Matéria: Tópicos de Mat. Apl. A'''
f=[]
print('Calcule o maior fator primo de qualquer número.\n\n')
n=int(input('Defina o número cujo maior fator primo deseja calcular: '))
j=n
print('')
for i in range(2,n+1):#todos os números ate um N definido para acharmos todos os possíveis divisores
        if n==1:
                break
        elif n%i==0:#se o resto é zero, temos um divisor
                f.append(i)
                while n%i==0:
                        n=n/i#dividimos pelo divisor para eliminarmos os expoentes da fatoração
t=len(f)
print('O número '+str(j)+' possui '+str(t)+' fatores primos. O maior deles é:')
print(f[-1])#último termo da lista
        
