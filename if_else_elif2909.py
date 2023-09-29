"""
Comandos Condicionais
-> if verifica uma condiçao e faz desvio da execuçao do  programa
"""

idade = int(input("Digite a idade:"))
if idade >= 18:  # se a idade for maior de 18 #entao
    print("é maior de idade")  # resposta verdadeira
elif idade == 18:  # senao se
    print("tem 18 anos")
else:
    print("é menor de idade")  # resposta falsa
