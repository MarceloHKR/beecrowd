Val = input().split()
A, B, C = map(float, Val)

TR = A * C / 2
Cir = 3.14159 * (C ** 2)
TP = (A + B) * C  / 2
Qua = B ** 2
Ret= A * B

print(f'TRIANGULO: {TR:.3f}')
print(f'CIRCULO: {Cir:.3f}')
print(f'TRAPEZIO: {TP:.3f}')
print(f'QUADRADO: {Qua:.3f}')
print(f'RETANGULO: {Ret:.3f}')

