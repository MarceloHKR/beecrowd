x = int(input())
y = int(input())

soma = 0
menor = min(x,y)
maior = max(x,y)

for i in range(menor , maior, 2):
    if(i % 2 != 0):
        soma += 1

print(soma)
