def dobrar(x):
    return x * 2

def trip(x):
    return x * 3

def quat(x):
    return x * 4

x = float(input("Digite o numero: "))
op2 = input("DTQ: ")

if op2 == "D" or op2 == "d":
    print(f"O resultado é {dobrar(x)}")
elif op2 == "T" or op2 == "t":
    print(f"O resultado é {trip(x)}")
elif op2 == "Q" or op2 == "q":
    print(f"O resultado é {quat(x)}")

#----------------------------------------

def multiplicador(mult):
    def mult2(num):
        return mult * num
    return mult2

dtq2 = multiplicador(2)
dtq3 = multiplicador(3)
dtq4 = multiplicador(4)

print(dtq2(2))
print(dtq3(2))
print(dtq4(2))

