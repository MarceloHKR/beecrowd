cord = input().split()
X = float(cord[0])
Y = float(cord[1])



if (X < 0) and (Y < 0):
  print('Q3')
elif(X == 0) and (Y != 0):
  print('Eixo Y')
elif(X != 0) and (Y == 0):
  print('Eixo X')
elif(X > 0) and (Y > 0):
  print('Q1')
elif(X > 0) and (Y < 0):
  print('Q4')
elif(X < 0) and (Y > 0):
  print('Q2')
else:
  print('Origem')