class Celular:
    cor = 'azul' 
    modelo = 'tijolao'
    marca = 'nokia'
    bateria = 'infinita'
    tem_camera = 'False'

def fazer_ligaçao(self):
   print('fazendo ligaçao....')

def jogando_cobrinha(self):
   print('jogando conbrinha....')

def despertador(self):
   print ('despertando...')

def calcular(self, v1, v2):
    return v1 + v2

celular = Celular()
calculado = celular.calcular(2,4)
print (calculado)

