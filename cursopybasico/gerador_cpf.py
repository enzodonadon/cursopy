
cpf = [7,4,6,8,2,4,8,9,0]

num_mult = 10
soma = 0
for i in cpf:
    mult = i * num_mult
    num_mult -= 1
    soma += (mult) 

mult2 = soma * 10

rest = mult2 % 11

primeiro_digito = rest if rest <= 9 else 0

print(primeiro_digito)