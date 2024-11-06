#Faça um programa que calcule o valor total de compra de máscaras contra a covid:
q=int(input("Insira a quantidade de máscara compradas:\n"))
if(0<q<100):
    v=6.0
    print(f"O valor das máscaras será por:\nR${v}")
else:
    if(100<q<200):
        v=5.0
        print(f"O valor das máscaras será por:\nR${v}")
    else:
        v=4.0
        print(f"O valor das máscaras será por:\nR${v}")
total=q*v
print(f"O lucro total foi:\nR${total:.2f}")