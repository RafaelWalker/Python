co = float(input('Informe o comprimento do Cateto Oposto: '))
ca = float(input('Informe o comprimento do Cateto Adjascente: '))
hi = (co**2 + ca**2) ** (1/2)
print('O comprimento da hipotenusa será: {:.2f}'.format(hi))