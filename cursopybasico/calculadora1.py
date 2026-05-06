print("Digite 1 para soma.")
print("Digite 2 para subtração.")
print("Digite 3 para divisão.")
print("Digite 4 para multiplicação.")
print("")
print("Digite 5 para sair.")
print("")

op = int(input(""))

while op != 5:
    if op == 1:
        print("Voce escolheu soma.")
        print("")
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        soma = num1 + num2
        print("")
        print(f"Resultado: {soma}")
        print("")
        op = int(input(""))

    elif op == 2:
        print("Voce escolheu subtração.")
        print("")
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        sub = num1 - num2
        print("")
        print(f"Resultado: {sub}")
        print("")
        op = int(input(""))   
    
    elif op == 3:
        print("Voce escolheu divisao.")
        print("")
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        div = num1 / num2
        print("")
        print(f"Resultado: {div}")
        print("")
        op = int(input(""))

    elif op == 4:
        print("Voce escolheu multiplicacao.")
        print("")
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        mult = num1 * num2
        print("")
        print(f"Resultado: {mult}")
        print("")
        op = int(input(""))
    elif op == 5:
        break
print("")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print("")
print("FIM DA EXECUCAO DO PROGRAMA.")