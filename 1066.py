n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())

par = 0
impar = 0
positivo = 0
negativo = 0

if n1 > 0:
    positivo += 1
    if n1 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n1 <0:
    negativo +=1
    if n1 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n1 == 0:
    par +=1

if n2 > 0:
    positivo += 1
    if n2 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n2 <0:
    negativo +=1
    if n2 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n2 == 0:
    par +=1

if n3 > 0:
    positivo += 1
    if n3 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n3 <0:
    negativo +=1
    if n3 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n3 == 0:
    par +=1

if n4 > 0:
    positivo += 1
    if n4 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n4 <0:
    negativo +=1
    if n4 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n4 == 0:
    par +=1

if n5 > 0:
    positivo += 1
    if n5 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n5 <0:
    negativo +=1
    if n5 % 2 == 0:
        par +=1
    else:
        impar+=1
elif n5 == 0:
    par +=1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')