from sys import path

import aula_packages_.modulo
from aula_packages import modulo
from aula_packages.modulo import soma

#print(*path, sep='\n')
print(soma(1, 2))
print(aula_packages.modulo.soma(1, 2))
print(modulo.soma(1, 2))