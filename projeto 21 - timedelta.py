from datetime import datetime, timedelta

tipo_carro = "P" # P,M,G
tempo_pequeno = 130
tempo_medio = 245
tempo_grande = 160

data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print (f' O carro chegou em {data_atual} e ficará pronto ás {data_estimada}')

elif tipo_carro =="m":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print (f' O carro chegou em {data_atual} e ficará pronto ás {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print (f' O carro chegou em {data_atual} e ficará pronto ás {data_estimada}')


