valor = input().split( )

a = float(valor[0])
b = float(valor[1])
c = float(valor[2])

delta = b * b - 4 * a * c

if delta < 0 or a==0:
    print('Impossivel calcular')
else:
    r1 = (-b + (delta**(1/2)))/(2*a)
    r2 = (-b - (delta**(1/2)))/(2*a)
    print(f'R1 = {r1 :.5f}')
    print(f'R2 = {r2 :.5f}')