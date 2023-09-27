# entrada de usuario atraves do input

#entrada
nome = input("Digite o seu nome")
idade = input("digie a sua idade")

# Processamento de dados

ano = 2023 - int(idade)

# saida

print("seja bem vindo", nome.title())
print(f"ola {nome.title()} , voce tem {idade} e nasceu em : {ano}") # o f é formato
