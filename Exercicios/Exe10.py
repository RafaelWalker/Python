valor = float(input('Quantos Reais você que Trocar para Dolar: '))
dolar = float(input('Informe o Valor do Dolar: '))
print('Com R$: {:.2f} você pode comprar US$: {:.2f}'.format(valor, (valor/dolar)))