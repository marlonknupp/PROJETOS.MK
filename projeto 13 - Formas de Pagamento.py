print('=========LOJAS KNUPP==========')
preço = float(input('Preço das compras: R$'))

print ('''FORMAS DE PAGAMENTO
       
[1] á vista dinheiro/cheque
[2] á vista cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão
-------------------------------''')
opção = float(input('Qual opção você deseja?'))
if opção ==1:
    total = preço - (preço * 10 / 100)
elif opção ==2:
    total = preço - (preço * 5 / 100)
elif opção ==3:
    total = preço
    parcela = total / 2
    print (f'Sua compra será parcelada em 2x de R$ {parcela} SEM JUROS.')
elif opção ==4:
    total = preço + (preço * 20 / 100)
    totparcelas = int(input('Quantas parcelas?'))
    parcela = total / totparcelas
    print (f'Sua compra será parcelada em {totparcelas}x de R${parcela:.2f} COM JUROS!')

print (f' Sua compra de {preço} custará {total} no final')