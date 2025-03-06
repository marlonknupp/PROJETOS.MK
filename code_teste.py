import pandas as pd

dados = [

    {'Nome':'luciana', 'Vendas': 120},
    {'Nome':'Valéria', 'Vendas': 140},
    {'Nome':'marcos', 'Vendas': 12},
    {'Nome':'josé', 'Vendas': 170},
    {'Nome':'luiz', 'Vendas': 10},
    {'Nome':'maria', 'Vendas': 139},
    {'Nome':'flores', 'Vendas': 110},

 ]

pd.DataFrame(dados). to_excel ('Planilha.xlsx')


