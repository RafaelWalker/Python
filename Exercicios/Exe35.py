cores = {'vermelho':'\033[31m',
         'azul':'\033[34m'}

print('{}-='.format(cores['vermelho']) *20)
print('{}     Analisador de Triângulos'.format(cores['azul']))
print('{}-='.format(cores['vermelho']) *20)
p1 = float(input('Digite o Primeiro Segmento: '))
p2 = float(input('Digite o Segundo Segmento:  '))
p3 = float(input('Digite o Terceiro Segmento: '))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os Segmentos Acima podem formar Triângulo')
else:
    print('Os Segmentos Acima não podem formar Triângulo!!')