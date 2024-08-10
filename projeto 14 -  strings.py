nome = str(input('Diga seu nome completo'))
primeironome = str(input('Diga seu primeiro nome'))

# Nome com todas as letras maiusculas 
# nome com todas as letras minusculas
# Quantas letras ao todo seu nome tem
# Quantas letras tem o primeiro nomee

print ('Analisando seu nome...')

print (f'Seu nome em MAIUSCULO {nome.upper()}')
print (f'Seu nome em minusculo{nome.lower()}')
print (f'Total de letras no seu nome {nome.__len__()}')
print (f' Seu primeiro nome tem {primeironome.__len__()} letras')
