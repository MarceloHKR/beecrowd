#importa uma biblioteca "atalho" nesse caso limpa o calculo anterior
import os
soma = 0
quant = 0
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



  if op == "1":
    a = float(input('Escolha o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    print(f'O resultado de {a} + {b} é {a+b}')
  elif op == '2':
    a = float(input('Escolha o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    print(f'O resultado de {a} - {b} é {a-b}')
  elif op == '3':
    a = float(input('Escolha o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    print(f'O resultado de {a} X {b} é {a*b}')
  elif op == '4':
    a = float(input('Escolha o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    print(f'O resultado de {a} : {b} é {a/b}')
  elif op == '5':
    a = float(input('Escolha o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    print(f'O resultado de {a} ^ {b} é {a**b}')
  elif op == '6':
    a = float(input('Escolha o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    print(f'O resultado de {a} X {b}% é {a*b/100}')
  elif op == '7':
    a = float(input('Escolha o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    print(f'O resultado de {a} : {b}% é {a/b*100 :.4f}')
  elif op == '8':
    for i in range(6):
        v = float(input())
        if v > 0:
            soma = soma + v
            quant = quant + 1
            r = soma / quant
        print(f'O resultado da diferença entre {a} e {b} é {r}')

#Escolha a operação:

# 1 - Adição
# 2 - Subtração
# 3 - Multiplicação
# 4 - Divisão

# Escolha a operação pelo número:

#trazer para a proxima aula
#adicionar quantos numeros quiser
#fazer as operações em ordem primeiro a multiplicação depois a soma e assim em seguida