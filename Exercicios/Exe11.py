largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
print('Sua parede tem a dimensão de {} X {} e sua Área é de {}m²'.format(largura, altura, (altura*largura)))
print('Para pintar essa parede, você precisará de {}l de tinta'.format((largura*altura)/2))