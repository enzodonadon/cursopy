import importlib
import modulos_inicio2 as modulos2

print(modulos2.nome)

for i in range(10):
    importlib.reload(modulos2)
    print(i)

print('Fim')