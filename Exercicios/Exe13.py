salario = float(input('Qual é o salário do Funcionário? R$: '))
aumento = float(input('Qual a porcentagem de aumento do salário %: '))
print('O Funcionário que ganhava {:.2f}, com 15% de aumento, vai receber R$: {:.2f}'.format(salario, (salario + (salario * aumento /100))))