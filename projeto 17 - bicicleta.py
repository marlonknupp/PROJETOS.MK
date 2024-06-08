class bicicleta: 
 def __init__(self,cor,modelo,ano,valor):
    self.cor = cor
    self.modelo = modelo
    self.valor = valor
    self.ano = ano

 def buzinar (self):
   print('plin, plin....')

 def parar (self):

  print('parando bicicleta')
  print('bicicleta parada')

 def correr (self):
  print('vrummmmmm...')


b1 = bicicleta ("vermelha", "caloi" , 2022 , 600)
b1.buzinar()
b1.parar()
b1.correr()
print(f'modelo: {b1.modelo} | cor:{b1.cor} | valor:{b1.valor}| ano:{b1.ano}')
