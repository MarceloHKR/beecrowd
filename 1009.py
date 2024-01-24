name = input('Digite seu Nome: ')
salary = float(input('Digite seu Salario: '))
vend = float(input('Digite seu número de vendas: '))

Com = vend * 0.15
t = salary + Com

print(f'TOTAL = R$ {t:.2f}')