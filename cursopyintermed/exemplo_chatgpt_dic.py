texto = "gato cachorro gato cavalo gato cachorro"
ocorrencias = {}

for palavra in texto.split():
    ocorrencias[palavra] = ocorrencias.get(palavra, 0) + 1

print(ocorrencias)
# {'gato': 3, 'cachorro': 2, 'cavalo': 1}