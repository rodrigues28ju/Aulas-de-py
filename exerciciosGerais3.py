import random
numeroSorteado = random.randint( 1, 10)
resp = 's'
print(numeroSorteado)
while resp == 's':
  chute = int(input("qual seu chute de 1 a 10?"))
  if chute == numeroSorteado:
      print('parabéns acertou!!!!!!!')
  else:
      print('errooooouuu!!!!')
  resp = input('quer continuar? s/n')