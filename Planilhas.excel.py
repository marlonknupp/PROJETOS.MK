import pandas as pd

# Dados das vendas
dados = [
    {'Nome': 'Vitória', 'Vendas': 120},
    {'Nome': 'Ana', 'Vendas': 50},
    {'Nome': 'Lucia', 'Vendas': 20},
    {'Nome': 'Maria', 'Vendas': 45},
    {'Nome': 'Luciana', 'Vendas': 450},
    {'Nome': 'Jaqueline', 'Vendas': 5320},
]

# Criar DataFrame
pd.DataFrame(dados) .to_excel("Planilhas.xlsx")

