#importa uma biblioteca "atalho" nesse caso limpa o calculo anterior
import os

while True:
  print('1 - Adição')
  print('2 - Subtração')
  print('3 - Multiplicação')
  print('4 - Divisão')
  print('5 - Elevação')
  print('6 - Porcentagem')
  print('7 - Porcentagem Inversa')
  print('8 - Difereça')


  op = input('Escolha a operação: ')
  os.system('cls')

  if op == '0':
    break

  for a in range(input()):

    if op == "1":
        print(f'O resultado de {a} é {a+a}')
    elif op == '2':
        print(f'O resultado de {a} - {b} é {a-b}')
    elif op == '3':
        print(f'O resultado de {a} X {b} é {a*b}')
    elif op == '4':
        print(f'O resultado de {a} : {b} é {a/b}')
    elif op == '5':
        print(f'O resultado de {a} ^ {b} é {a**b}')
    elif op == '6':
        print(f'O resultado de {a} X {b}% é {a*b/100}')
    elif op == '7':
        print(f'O resultado de {a} : {b}% é {a/b*100 :.4f}')
    elif op == '8':
        print(f'O resultado da diferença entre {a} e {b} é {a+b/2}')

#Escolha a operação:

# 1 - Adição
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão

# Escolha a operação pelo número:

#trazer para a proxima aula
#adicionar quantos numeros quiser
#fazer as operações em ordem primeiro a multiplicação depois a soma e assim em seguida