import random
aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
lista = [aluno1, aluno2, aluno3]
resultado = random.choice(lista)
print('O Aluno sorteado foi ',resultado)