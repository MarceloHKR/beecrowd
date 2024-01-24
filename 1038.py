

escolha, quantidade = map(int,input().split())

valor = 0

if escolha == 1:
    valor = 4.0
elif escolha == 2:
    valor = 4.5
elif escolha == 3:
    valor = 5.0
elif escolha == 4:
    valor = 2.0
elif escolha == 5:
    valor = 1.5

print(f'Total: R$ {valor*quantidade:.2f}')


'''id, quantidade = map(int, input().split())
valor = 0

if id == 1:
    valor = 4.0
elif id == 2:
    valor = 4.5
elif id == 3:
    valor = 5.0
elif id == 4:
    valor = 2.0
elif id == 5:
    valor = 1.5

print(f'Total: R$ {valor*quantidade:.2f}')'''

