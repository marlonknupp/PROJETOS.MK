def recomendar_plano(consumo): 


 if consumo <= 10:
       return 'Plano Essencial Fibra - 50Mbps'
 
 elif consumo > 10 and consumo <= 20:
       return 'Plano Prata Fibra - 100Mbps'
    
 elif consumo > 20:
       return 'Plano Premium Fibra - 300Mbps'
    
 else:
       return
 

consumo = float(input('Insira seu consumo médio mensal de internet: '))

print ('O plano recomendado para voce é:', recomendar_plano(consumo))
