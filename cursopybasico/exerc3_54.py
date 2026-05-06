nome = input("Qual seu nome? ")
tnome = len(nome)

if tnome >= 1:
    if tnome == 1:
        print("Digite mais de uma letra.")
    elif tnome <= 4:
        print("Seu nome é curto.")
    elif tnome == 5 or tnome == 6:
        print("Seu nome é normal.")
    elif tnome > 6:
        print("Seu nome é grande.")
else:
    print("Digite algo.")