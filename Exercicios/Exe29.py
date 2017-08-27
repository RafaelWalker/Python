velocidade = int(input('Informe a velocidade do Veículo: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Atenção! Limite de velocidade excedido!!!')
    print('A velocidade máxima é de 80km e você está a {}km'.format(velocidade))
    print('Você foi multado em R$: {:.2f}'.format(multa))
else:
    print('Parabéns sua velocidade é: {}km, você está no limite de velocidade!'.format(velocidade))
print('Tenha um bom dia!  Dirija com segurança!' )
