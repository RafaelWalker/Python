# primeiro parametro colchetes tipo de fonte, segundo cor da fonte e terceiro com fundo
print('\033[1;31;43mOlá Mundo!\033[m')

#segundo modo
nome = 'Rafael'
print('Olá! Segundo teste de cor {}{}{}'.format('\033[4;34m', nome, '\033[m'))

#terceiro modo
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('-----------------------------------------------------------')

print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))