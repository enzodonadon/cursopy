import os, time

listar = []

while True:   
    
    print("Selecione uma opção: ")
    opcoes = input("[i]nserir  [a]pagar   [l]istar: ")
    
    if opcoes != "i" and opcoes != "a" and  opcoes != "l":
        tempo = 3
        for seg_rest in range(tempo, 0, -1):
            print(f"Opção invalida. Tentando novamente em {seg_rest} segundos...", end="\r") 
            time.sleep(1)
        os.system('cls')

    if opcoes == "i":
        os.system('cls')
        nome = input("Insira o nome do produto: ")
        listar.append(nome)
        
    if opcoes == "a":
        if len(listar) == 0:
            print("Nada há apagar.")
        indice_str = input("Qual o indice que deseja apagar? ")
        try:
            indice = int(indice_str)
            del listar[indice]
        except ValueError:
            print('Por favor digite número inteiro.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
        
    if opcoes == "l":
        os.system('cls')
        if len(listar) == 0:
            print("Nada há listar.")
        else:
            print("Listagem: ")
            for i, n in enumerate(listar):
                print(f'{i} : {n}')

    


