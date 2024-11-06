#Faça um programa em que o usuário pode escolher a realização de uma das quatro operações básicas:
n1=float(input("Insira um número:\n"))
n2=float(input("Insira outro número:\n"))
op=int(input("Insira o número relacionado ao sinal de operação desejado para realizar o cálculo:\n+=1\n-=2\nx=3\n/=4\n"))
if(op>=5):
    print("Não foi possível realizar a operação. Por favor, escolha um número de 1 a 4.")
elif(op==0):
    print("Não foi possível realizar a operação. Por favor, escolha um número de 1 a 4.")
elif(op==1):
    r=n1+n2
    print(f"O resultado da soma é:\n{r}")
elif(op==2):
    r=n1-n2
    print(f"O resultado da subtração é:\n{r}")
elif(op==3):
    r=n1*n2
    print(f"O resultado da multiplicação é:\n{r}")
elif(op==4):
    if(n2==0):
        print("Não é possível dividir por zero.")
    else:
        r=n1/n2
        print(f"O resultado da divisão é:\n{r}")