import os
list = []
print('---------------------------------------------------------------------------------------------------')
print('Bem-vindo ao nosso gerenciador de tarefas, a sua solução completa para organização e produtividade! Estamos empolgados em tê-lo a bordo para ajudá-lo a simplificar sua vida e alcançar seus objetivos de maneira mais eficaz.')
print('')
print('Com nosso poderoso conjunto de recursos, você terá o controle total sobre suas tarefas, metas e projetos. Não importa se você é um profissional ocupado, um estudante determinado ou alguém que simplesmente busca mais ordem em seu dia a dia, estamos aqui para tornar sua jornada mais fácil e eficiente.')
print('')
print('Então, comece a explorar e descobrir como nosso gerenciador de tarefas pode facilitar sua vida e permitir que você se concentre no que realmente importa.')
print('')
print('O sucesso está à sua espera!')
print('')
while True:
  print('---------------------------------------------------------------------------------------------------')
  print('Tarefas:')
  print(list)
  print('')
  print('---------------------------------------------------------------------------------------------------')
  print('- Opção 1: Adicionar uma nova tarefa à lista.')
  print('- Opção 2: Exibir todas as tarefas existentes.')
  print('- Opção 3: Marcar uma tarefa como concluída.')
  print('- opção 4: Marcar todas as tarefas como concluídas.')
  print('- Opção 5: Sair do programa.')
  print('')
  print('')

  op = input('O que você deseja? ')
  os.system('cls')

  if op == '5':
    break

  elif op == '1':
    list.append(input('A seguinte tarefa será adicionada: '))
  elif op == '2':
    print(list)
  elif op == '3':
    list.remove(input('Qual tarefa deseja marcada como concluída: '))
  elif op == '4':
    list.clear()