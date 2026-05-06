
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


cont = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print('Opções: ')
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i+1}) {opcao}')
    resposta = int(input('Escolha uma opção:'))
    
    for i, opcao in enumerate(pergunta['Opções']):
        if opcao == pergunta['Resposta']:
            if resposta == i + 1:
                print('Você acertou!')
                print()
                cont += 1
            else:
                print('Você errou.')
                print()
print(f'Você acertou {cont} de {len(perguntas)} perguntas.')
