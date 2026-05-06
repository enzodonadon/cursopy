numeros = input("Digite números separados por vírgula: ").split(',')

dobrados = []
for n in numeros:
    dobrar = lambda x: int(x) * 2
    dobrados.append(dobrar(n))
    
print(dobrados)

