
Menu = ('***')

print ("""
       
**
[1] depositar 
[2] sacar 
[3] extrato
[4] sair 

*** 
""")

saldo = 0
limite = 500
extrato = '***'
numero_saques = 0 
LIMITE_SAQUES = 3 

while True:

 opçao = input('Menu')

 if opçao =='1':
    valor = float(input('Informe o valor do depósito'))

    if valor >0:
        saldo == valor
        extrato == f'Depósito: R$ {valor:.2f}\n'

    else:
     print ('operaçao falhou! O valor Informado é inválido')

 elif opçao == '2':
    Valor = float(input('Informe o valor do saque:'))
    
    excedeu_saldo = valor > saldo
    
    excedeu_limite = valor > limite
    
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
       print ('Operaçao falhou! Voce nao tem saldo suficiente')
    
    elif excedeu_limite: 
       print ('Operaçao falhou! O valor do saque excede o limite')
    
    elif excedeu_saques:
       print ('Operaçao falhou! Numero máximo de saques excedido')

    elif valor >0:
       saldo -= valor
       extrato += f'saque: R$ {valor:.2f}\n'
       numero_saques += 1
    

    else:
       print ('Operaçao Falhou, O valor informado é inválido')


 elif opçao == 'e':
   
    print ('\n=======================EXTRATO=====================')
    print ('Nao foram realizado movimentaçoes' if not extrato else extrato)
    print (f'\n saldo: R$ {saldo:.2f}')
    print ('==========================================')

 elif opçao == '4':
  break 
 
 else:
    print ('Operaçao inválida, por favor tente novamente a opçao desejada')