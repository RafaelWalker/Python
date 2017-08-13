#.strip() tira espaços em branco no inicio e no final
nome = str(input('Digite seu Nome Completo: ')).strip()
print(nome)
print('Agora seu nome em letras Maiúsculas {}'.format(nome.upper()))
print('Agora deu nome em letras Minúsculas {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu Primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))