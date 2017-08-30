salario = float(input('Informe o valor do Salário do Funcionário: '))
if salario > 1250:
    print('Com o Aumento seu salário será de R$: {:.2f}'.format(salario + ((salario * 10) / 100)))
else:
    print('Com o aumento seu salário será de R$: {:.2f}'.format(salario + (salario * 15)/ 100))