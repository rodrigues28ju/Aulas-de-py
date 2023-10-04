"""
criar programa que leia dois numeros e informe
o maiior deles
"""
n1 = int(input('digite primeiro numero:'))
n2 = int(input('digite o segundo numero:'))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 == n2:
    print(f'são iguais')
else:
    print(f'{n2} é maior que {n1}')
