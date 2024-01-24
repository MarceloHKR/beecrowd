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

  if op == "1":
    expre = input("Digite a sua expressão de soma: ")
    lista_str = expre.split('+')
    lista_num = []
    for numero in lista_str:
      lista_num.append(int(numero.strip()))
    print(f'O resultado de {expre} é {sum(lista_num)}')
  elif op == '2':
    expre = input("Digite a sua expressão de subtração: ")
    numeros_str = expre.split("-")
    resultado = float(numeros_str.pop(0))
    for numero in numeros_str:
      resultado -= float(numero.strip())
    print(f'O resultado de {expre} é {resultado}')
  elif op == '3':
    expre = input("Digite a sua expressão de multiplicação: ")
    numeros_str = expre.split("*")
    resultado = float(numeros_str.pop(0))
    for numero in numeros_str:
      resultado -= float(numero.strip())
    print(f'O resultado de {expre} é {resultado}')
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


