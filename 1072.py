n = int(input())
in1 = 0
out1 = 0

for i in range(n):
    x = int(input())
    if (x >= 10) and (x <= 20):
        in1 += 1 
    else:
        out1 += 1

print(f'{in1} in')
print(f'{out1} out')