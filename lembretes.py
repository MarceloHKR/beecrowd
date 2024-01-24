#Lista vazia
lista = []
print(lista)

#Lista com nomes e numeros
lista = ['O carro', 'abacaxi', 123, 5.5]
print(lista)

#
nova_lista = ['Turing', lista]
print(nova_lista)

#mostra um item expecifico da lista
print(lista[0])

#mostra os itens de uma lista dentro de outra lista
print(nova_lista[1][2])

#junta as listas
lista_2 = ['Joui', 'Arthur', 'Kaiser']
listao = ['Liz', 'Thiago', 'Cristofer']
result = lista_2 + listao
print(result)

#multiplica a lista
print(lista * 3)

#mostra a quantidade de intens dentro da lista
print(len(lista))

#mostra se existe essa palavra na lista
print('banana' in lista_2)
print('Kaiser' in lista_2)

#usar mais o W3Schools!!!!!!!

#faz uma copia de uma lista sem auterala
lista_copia = lista_2.copy()
print(lista_copia)

#adiciona itens na lista
list.append(input())

#---------------------------------------------------------------------#

#loops
#for = para
#while = enquanto / o comando vai repetir até o i não ser menor que 6 para conseguir um numero expecifico adicione um numero a mais no caso o que vai ser somado no valor
#exp:se eu quero 100 e vai somando 2 a partir do zero eu preciso colocar 102
i = 1
while i < 6:
  print(i)
  i += 1

#break: quando i=3 o loop para imediatamente
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

#continue: faz o loop até chegar no 6 mas não mostra o número 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#for: ele vai printar a lista até acabar os elementos
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#printa cada letra da palavra
for x in "banana":
  print(x)

#vai printar até chagar em banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#para de printar quando chegar em banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#range: espaço entre as prints
#vai printar do 0 ao 5
for x in range(6):
  print(x)

#vai printar a partir do primeiro número até o ultimo
for x in range(2, 6):
  print(x)

#vai printar do 2 até o 30 pulando 3 em 3 números
for x in range(2, 30, 3):
  print(x)


#-----------------------------------------------------------------------------
#Versões tipo 1.01.2

#main é o inicio de um código
#Branch é um ramo que você cria para ceparar um código do código principal