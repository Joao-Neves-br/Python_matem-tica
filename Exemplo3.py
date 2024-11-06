#Como calcular a média de um aluno:
n1=float(input("Insira a sua 1° nota:\n"))
n2=float(input("Insira a sua 2° nota:\n"))
m=(n1+n2)/2
if(0<=m<2):
    print("Infelizmente, você foi reprovado.")
elif(2<=m<7):
    print("Vocẽ está na final. Ainda tem chance!")
else:
    print("Parabéns, você foi aprovado!")