n1, n2, n3, n4 = map(float, input().split())

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10


print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    resultado = (media + exame) / 2
    if resultado <= 4.9:
        print('Aluno reprovado.')
    elif resultado >= 5.0:
        print(f'Nota do exame: {exame}')
        print('Aluno aprovado.')
        print(f'Media final: {resultado:.1f}')