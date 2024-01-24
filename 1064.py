soma = 0
quant = 0

for i in range(6):
    v = float(input())
    if v > 0:
        soma = soma + v
        quant = quant + 1
        r = soma / quant
print(f'{quant} valores positivos')
print(f'{r :.1f}')