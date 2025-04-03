import pandas as pd

dados = [
    {"nome":"marlon","vendas":"120"},
    {"nome":"marlon","vendas":"150"},
    {"nome":"marlon","vendas":"1230"},
    {"nome":"marlon","vendas":"1220"},
    {"nome":"marlon","vendas":"120"},
    {"nome":"marlon","vendas":"120"},
    {"nome":"marlon","vendas":"120"},
]

pd.DataFrame(dados).to_excel ("planilha.xlsx")