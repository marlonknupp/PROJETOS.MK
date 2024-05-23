Vel = int(input('Qual a velocidade atual do seu carro?'))

if Vel >80:
    multa = (Vel - 80) * 7  # 7 REAIS POR CADA KM ACIMA DO LIMITE
    print (f'MULTADO, você excedeu o limite permitido que é de 80km/h \n você deve pagar uma multa de R$ {multa},00 \n TENHA UM BOM DIA, DIRIJA COM SEGURANÇA')

else: 
    print ('Tudo certo com a velocidade. Òtimo dia!')