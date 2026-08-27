import importlib
import modulos2

print(modulos2.nome)

for i in range(10):
    importlib.reload(modulos2)
    print(i)

print('Fim')