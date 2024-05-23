MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade'))

if idade >= MAIOR_IDADE:
    print('Parabéns, voce ja pode tirar sua carteira')

elif idade == IDADE_ESPECIAL:
    print ('Pode executar, mas nao pode tirar. ATENÇAO!!!!!!')

else:
   print('Infelizmente nao pode tirar sua carteira')

