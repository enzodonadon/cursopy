entrada = (input("Digite o horário: "))
try:
    hor = int(entrada)

    if hor < 0 or hor > 23:
        print("Horário inválido. Tente novamente.")
    else:    
        if hor >= 0 and hor <= 11:
            print("Bom dia!")
        elif hor >= 12 and hor <= 17:
            print("Boa tarde!")
        elif hor >= 18 and hor <= 23:
            print("Boa noite!")      
except:
    print("Digite um número inteiro.")