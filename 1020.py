dias = int(input())

ano = int(dias / 365)
dias_restantes = dias % 365

mes = int( dias_restantes / 30)
dias = dias_restantes%30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')

