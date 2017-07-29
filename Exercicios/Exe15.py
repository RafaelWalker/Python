km = int(input('Informe qual a Quantidade de Km percorridos: '))
dia = int(input('Informe Quantos dias você ultilizou o Carro: '))
total = (km*0.15) + (dia*60)
print('O Total a pagar é de R${:.2f}'.format(total))