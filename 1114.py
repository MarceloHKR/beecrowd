senha = 2002


for i in senha:
    i = int(input())
    if i != senha:
        print('Senha Invalida')
    elif i == senha:
        print('Acesso Permitido')