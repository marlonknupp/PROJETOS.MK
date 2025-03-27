import pandas as pd 

dados = [
    {'Nome':'Luciana','Vendas': 1420},
    {'Nome':'marlon','Vendas': 1620},
    {'Nome':'maria','Vendas': 1330},
    {'Nome':'penelope','Vendas': 1803},
    {'Nome':'jhonata','Vendas': 1220},
    {'Nome':'andré','Vendas': 12340},
    {'Nome':'Lucia','Vendas': 1220},
    {'Nome':'mariana','Vendas': 1220},
]

pd.DataFrame(dados).to_excel ('planilha.xlsx')