print('Você abriu "Palavra Secreta".')
print("")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print("")

tent = 0
palavra = "penta"
letra_acertada = ""


while True:
    
    letra = input("Digite uma letra: ")
    cont = len(letra)
    while cont >= 2 or "1" in letra or "2" in letra or "3" in letra or "4" in "letra" or "5" in letra or "6" in letra or "7" in letra or "8" in letra or "9" in letra or "0" in letra: 
        letra = input("Opcao invalida. Digite apenas uma letra: ")
        cont = len(letra)
    
    if letra in palavra:
        letra_acertada += letra

    palavraformat = ""
    
    for letra1 in palavra:
        
        if letra1 in letra_acertada:
            palavraformat += letra1
        else:
            palavraformat += "*"
    tent += 1
    print(palavraformat)
    
    
    if palavraformat == palavra:
        break
print (f"Parabéns, voce acertou em {tent} tentativa(s)")
        
    
    
    

    





