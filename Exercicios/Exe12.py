preco = float(input('Qual o preço do produto? R$: '))
print('O produto que custava R$: {}, na promoção com desconto de 5% vai custar R$: {:.2f}'.format(preco, (preco - (preco *5 /100))))