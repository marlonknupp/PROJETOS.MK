class carro:
    numero_rodas = 4
    quantidade_passageiros = 5 

    def acelerar (self):
        print('acelerando....')
    
    def frear (self):
        print('freando...')

    def buzinar(Self):
        print('buzinando...')


class Uno (carro):
    modelo = 'uno'
    marca = 'fiat'
    ano =  '1993'
    numerp_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self):
        print('acelerando...')
    
    def frear(self):
        print('freandoooooooo')

    def buzinar(Self):
        print('buzinandooo')
    
uno = Uno()
uno.acelerar()