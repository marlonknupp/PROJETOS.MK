from random import randint
computador = randint (0,10)  # FAZ O COMPUTADOR PENSAR

print ('-------------------------')
print (' Vou pensar em um numero de 0 a 10 - tente advinhar...')
print ('--------------------------')

jogador = int(input(' Em que numero eu pensei?'))    #JOGADOR TENTANDO ADVINHAR

if jogador == computador:
    print('PARABÉNS, VOCE CONSEGUIU ME VENCER!')

else:
    print(f'VOCÊ ERROU, BOA SORTE NA PROXIMA!')

print (f' {computador}')