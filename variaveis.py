aluno = "Juliana"  # criada variavél auluno  e nota com dados
nota = 10
print(aluno)  # criado o conteudo da variável aluno
print(nota)
print(type(aluno))  # exibe  o tipo de dado que o dado está recebendo que pode ser string etc...
print(type(nota))

# https://www.w3schools.com/python  versão 3

paciente = "João Da Silva Moreira"
print(
    paciente.title())  # a função lower e para jogar as letras minusculas, e o upper para Maiuscula e o title colaca
# primeira letra de cada palavra maiscula
# cuidado com os espaços pois o py e chato com identaçao https://peps.python.org/pep-0008/

# formas de escrita

myVariableName = "John"  # Camel Case
MyVariableName = "John"  # Pascal Case
my_variable_name = "John"  # Snake Case

# declaraçao de multiplas variaveis

a, b, c = "banana", "maça", "abacaxi"
print(a)
print(b)
print(c)

# declaraçao de multiplas variaveis com um unico valor

x = y = z = "laranja"

print(x, y, z)

# desempacotando coleçao

frutas = ["apple", "banana", "cherry"]  # vetor array lista
f1,f2,f3 = frutas
print(f1,f2,f3)
