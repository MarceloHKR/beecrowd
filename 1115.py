

while True:
    cord = input().split()
    X = float(cord[0])
    Y = float(cord[1])

    if X == 0 or Y == 0:
        break
    elif (X < 0) and (Y < 0):
        print('terceiro')
    elif(X > 0) and (Y > 0):
        print('primeiro')
    elif(X > 0) and (Y < 0):
        print('quarto')
    elif(X < 0) and (Y > 0):
        print('segundo')


