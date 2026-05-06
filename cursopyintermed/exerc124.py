cont = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
print(f"Pergunta: {perguntas[0]['Pergunta']}")
print("")
print("Opções: ")
for i, j in enumerate(perguntas[0]['Opções']):
    print(f"{i + 1}) {j}")
op1 = input("Escolha uma opção: ")
if op1 != "3": 
    print("Você errou.")
else:
    cont = cont + 1
    print("Você acertou!")

print("")

print(f"Pergunta: {perguntas[1]['Pergunta']}")
print("")
print("Opções: ")
for i, j in enumerate(perguntas[1]['Opções']):
    print(f"{i + 1}) {j}")
op1 = input("Escolha uma opção: ")
if op1 != "1": 
    print("Você errou.")
else:
    cont = cont + 1
    print("Você acertou!")

print("")

print(f"Pergunta: {perguntas[2]['Pergunta']}")
print("")
print("Opções: ")
for i, j in enumerate(perguntas[2]['Opções']):
    print(f"{i + 1}) {j}")
op1 = input("Escolha uma opção: ")
if op1 != "2": 
    print("Você errou.")
else:
    cont = cont + 1
    print("Você acertou!")

print("")

print(f"Você acertou {cont} questões.")

#------------------------------------------------------------

'''
qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
'''
