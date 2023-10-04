"""
crie um programa que calcule o valor de um carro
somando à ele o ICMS de 3.5%(0,035) se o valor for maior que 40000
senão o valor do ICMS será de 7,5%(0.075)

"""
valor = int(input('digite o valor do carro:'))

if valor >= 40000:
    icms = 40000 * 0.035
    print(f'valor icms: {icms}')
    print('valor final do carro:', valor +icms)


else:
    icms = 40000 * 0.075
    print(f'valor icms: {icms}')
    print('valor final do carro:', valor + icms)