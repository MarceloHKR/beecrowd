x = input().split()
play = int(x[0])
end = int(x[1])

if play < end:
    tempo = end - play
else:
    tempo = (24 - play) + end

print(f'O JOGO DUROU {tempo} HORA(S)')