n = str(input('Digite seu nome Completo: ')).strip()
nome = n.split()
print('O seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))