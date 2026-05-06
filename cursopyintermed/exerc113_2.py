def mult(*args):
    global total
    total = 0
    for num in args:
        if total == 0:
            total = num
        else:
            total *= num
    return total

def par_ou_impar():
    if total % 2 == 0:
        return f"{total} é par"
    return f"{total} é ímpar"
    
print(mult(2, 3, 4))
print(par_ou_impar())