print("Voce abriu Calculadora.")
print("")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print("")

c_or_s = input('Digite "C" para comecar e "S" para sair: ')
while c_or_s != "C" and c_or_s != "S" and c_or_s != "c" and c_or_s != "s" :
    c_or_s = input("Tente novamente: ")

while c_or_s != "S" and c_or_s!= "s":
    
    num1 = input("Digite o primeiro numero: ")
    cond = None
    while cond is None:
        try:
            num1_float = float(num1)
            cond = True
        except:
            num1 = input("Digite um numero valido: ")
            cond = None
            
    op = input("Digite um operador (+-*/): ")
    while op != "+" and op != "-" and op != "/" and op != "*":
        op = input("Digite um operador válido: ")

    if op == "+":
        num2 = input("Digite o segundo numero: ")
        cond = None
        while cond is None:
            try:
                num2_float = float(num2)
                cond = True
            except:
                num2 = input("Digite um numero valido: ")
                cond = None
        result = num1_float + num2_float
        print("Resultado: ", result)

    elif op == "-":
        num2 = input("Digite o segundo numero: ")
        cond = None
        while cond is None:
            try:
                num2_float = float(num2)
                cond = True
            except:
                num2 = input("Digite um numero valido: ")
                cond = None
        result = num1_float - num2_float
        print("Resultado: ", result)
    elif op == "/":
        num2 = input("Digite o segundo numero: ")
        cond = None
        while cond is None:
            try:
                num2_float = float(num2)
                cond = True
            except:
                num2 = input("Digite um numero valido: ")
                cond = None
        result = num1_float / num2_float
        print("Resultado: ", result)
    elif op == "*":
        num2 = input("Digite o segundo numero: ")
        cond = None
        while cond is None:
            try:
                num2_float = float(num2)
                cond = True
            except:
                num2 = input("Digite um numero valido: ")
                cond = None
        result = num1_float * num2_float
        print("Resultado: ", result)  

    print("")
    
    c_or_s = input("Deseja sair? [S]im ou [N]ao: ")
    while c_or_s != "S" and c_or_s != "N" and c_or_s != "s" and c_or_s != "n":
        c_or_s = (input("Digite um digito valido: [S] ou [N]: "))
        
        

print("")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print("")
print("FIM DA EXECUCAO DO PROGRAMA.")