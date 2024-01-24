while True:
  m, n = input().split(' ')
  m = int(m)
  n = int(n)
  if m <= 0 or n <= 0:
    break
  l = [m, n]
  m = min(l)
  n = max(l)
  soma = 0
  for i in range(m, n + 1):
    print(i, end=' ')
    soma += i
  print(f'Sum={soma}')
