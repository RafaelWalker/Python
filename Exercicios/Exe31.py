distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km'.format(distancia))
if distancia > 200:
   preco = distancia * 0.45
else:
    preco = distancia * 0.50
print('E o preço de sua passagem será de R$: {:.2f}'.format(preco))