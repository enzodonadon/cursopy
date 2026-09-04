from sys import path

import packages_1.modulo
from packages_1 import modulo
from packages_1.modulo import soma

#print(*path, sep='\n')
print(soma(1, 2))
print(packages_1.modulo.soma(1, 2))
print(modulo.soma(1, 2))