# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import modulos2 as mod

print('Este módulo se chama', __name__, 'arquivo 1')

print(mod.soma(5, 10))

#modulo.atributo - variavel (dado fixo)
# #modulo.funcao() - ação (uma rotina que faz um cálculo ou operação)

