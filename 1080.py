maior = -1
pos = 0
for i in range(100):
  a = int(input())
  if a > maior:
    maior = a
    pos = i + 1
print(maior)
print(pos)

#ou

numeros = []
for i in range(100):
  a = int(input())
  numeros.append(a)
maior = max(numeros)
pos = numeros.index(maior) + 1
