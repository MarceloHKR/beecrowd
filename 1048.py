salario = float(input())

if (salario >= 0) and ( salario <= 400.00):
    mult = salario * 0.15
    soma = mult + salario
    print(f'Novo salario: {soma:.2f}')
    print(f'Reajuste ganho: {mult:.2f}')
    print(f'Em percentual: 15 %')
elif (salario >= 400.01) and ( salario <= 800.00):
    mult = salario * 0.12
    soma = mult + salario
    print(f'Novo salario: {soma:.2f}')
    print(f'Reajuste ganho: {mult:.2f}')
    print(f'Em percentual: 12 %')
elif (salario >= 800.01) and ( salario <= 1200.00):
    mult = salario * 0.10
    soma = mult + salario
    print(f'Novo salario: {soma:.2f}')
    print(f'Reajuste ganho: {mult:.2f}')
    print(f'Em percentual: 10 %')
elif (salario >= 1200.01) and ( salario <= 2000.00):
    mult = salario * 0.07
    soma = mult + salario
    print(f'Novo salario: {soma:.2f}')
    print(f'Reajuste ganho: {mult:.2f}')
    print(f'Em percentual: 7 %')
elif (salario > 2000.00):
    mult = salario * 0.04
    soma = mult + salario
    print(f'Novo salario: {soma:.2f}')
    print(f'Reajuste ganho: {mult:.2f}')
    print(f'Em percentual: 4 %')
