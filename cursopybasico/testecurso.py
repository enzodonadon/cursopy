curso1 = input("Nome do primeiro curso extra: ")
curso2 = input("Nome do segundo  curso extra: ")
qtde_alunos = int(input("Quantidade de alunos da classe do 9o ano: "))

nomes  = []
sexos  = []
idades = []
cursos1 = []
cursos2 = []

for x in range(qtde_alunos):
    nome = input("Nome do aluno: ")
    sexo = input("Sexo: ")
    idade = input("Idade: ")
    nomes.append(nome)
    sexos.append(sexo)
    idades.append(idade)
     
    participar = input("Deseja participar de algum curso extra (S/N)?")
    if participar != "S" and participar != "N":
        print("Opcao invalida. Curso extra foi recusado.")
    else:
        if participar == "S":
            curso10 = input("Informe 1 para curso 1, 2 fazer o curso 2, ou 3 para fazer os dois cursos extras:")
            if curso10 == "1":
                cursos1.append(nome)
            if curso10 == "2":
                cursos2.append(nome)
            if curso10 == "3":
                cursos1.append(nome)                
                cursos2.append(nome)
        else:
            print("Aluno nao quer participar de curso extra")        

print("Alunos cadastrados no 9o ano")
print("")
print("Nome;Sexo;Idade")
for i in range(qtde_alunos):
    linha = nomes[i] + ";" + sexos[i] + ";" + idades[i]
#    imprime_nome = nomes[i]
#    imprime_sexo = sexos[i]
#    imprime_idade = idades[i]
#    linha = "{nome}, {sexo}, {idade} ".format(nome = imprime_nome, sexo = imprime_sexo,  idade = imprime_idade)
    print(linha)            

print("")
# curso01 = "Alunos cadastrados no curso 1 {curso}".format(curso = curso1)
curso01 = "Alunos cadastrados no curso 1 " + curso1
print(curso01)
for i in cursos1:
    print(i)
 

print("")
# curso02 = "Alunos cadastrados no curso 2 {curso}".format(curso = curso2)
curso02 = "Alunos cadastrados no curso 2 "+ curso2
print(curso02)
for i in cursos2:
  print(i)

print("")
print("-/-/-/-/-/-/-/-/-/-")
print("")
print("FIM")
