'''valor = float(input())

n100 = valor / 100
n50 = valor % 100 / 50
n20 = valor % 50 / 20
n10 = valor % 20 / 10
n5 = valor % 10 / 5
n2 = valor % 5 / 2

m1 = valor % 2 / 1
m50 = valor % 1 / 0.50
m25 = valor % 0.50 / 0.25
m10 = valor % 0.25 / 0.10
m5 = valor % 0.10 / 0.05
m01 = valor % 0.05 / 0.01

print(f'NOTAS:')
print(f'{n100 :.0f} nota(s) de R$ 100.00')
print(f'{n50 :.0f} nota(s) de R$ 50.00')
print(f'{n20 :.0f} nota(s) de R$ 20.00')
print(f'{n10 :.0f} nota(s) de R$ 10.00')
print(f'{n5 :.0f} nota(s) de R$ 5.00')
print(f'{n2 :.0f} nota(s) de R$ 2.00')

print('MOEDAS:')

print(f'{m1 :.0f} moeda(s) de R$ 1.00')
print(f'{m50 :.0f} moeda(s) de R$ 0.50')
print(f'{m25 :.0f} moeda(s) de R$ 0.25')
print(f'{m10 :.0f} moeda(s) de R$ 0.10')
print(f'{m5 :.0f} moeda(s) de R$ 0.05')
print(f'{m01 :.0f} moeda(s) de R$ 0.01')'''

reais, centavos = map(int, input().split('.'))
centavos = centavos + reais*100

print('NOTAS:')
print(f'{centavos//10000} nota(s) de R$ 100.00')
centavos = centavos%10000
print(f'{centavos//5000} nota(s) de R$ 50.00')
centavos = centavos%5000
print(f'{centavos//2000} nota(s) de R$ 20.00')
centavos = centavos%2000
print(f'{centavos//1000} nota(s) de R$ 10.00')
centavos = centavos%1000
print(f'{centavos//500} nota(s) de R$ 5.00')
centavos = centavos%500
print(f'{centavos//200} nota(s) de R$ 2.00')
centavos = centavos%200

print('MOEDAS:')
print(f'{centavos//100} moeda(s) de R$ 1.00')
centavos = centavos%100
print(f'{centavos//50} moeda(s) de R$ 0.50')
centavos = centavos%50
print(f'{centavos//25} moeda(s) de R$ 0.25')
centavos = centavos%25
print(f'{centavos//10} moeda(s) de R$ 0.10')
centavos = centavos%10
print(f'{centavos//5} moeda(s) de R$ 0.05')
centavos = centavos%5
print(f'{centavos//1} moeda(s) de R$ 0.01')
centavos = centavos%1