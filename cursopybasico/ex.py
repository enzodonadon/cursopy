numint = int(input("Digite um número inteiro: "))
par = numint % 2 == 0
if numint:
   if par:
    print("É um número par")
   else:
    print("É um número ímpar")