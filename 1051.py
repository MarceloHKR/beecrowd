Renda = float(input())

if (Renda >= 0) and ( Renda <= 2000.00):
    print('Isento')
elif (Renda > 2000.00) and ( Renda <= 3000.00):
    conta = (Renda - 2000.0) * 0.08
    print('R$ %.2f'%conta)
elif (Renda > 3000.00) and ( Renda <= 4500.00):
    conta = (Renda - 3000.0) * 0.18 + (1000*0.08)
    print('R$ %.2f'%conta)
elif ( Renda > 4500.00):
    conta = (Renda - 4500)*0.28 + (1500*0.18) + (1000*0.08)
    print('R$ %.2f'%conta)