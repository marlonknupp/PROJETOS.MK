import openpyxl
import openpyxl.workbook

# criar uma planilha
book = openpyxl.Workbook()

# Visualiza pagina existente
print (book.sheetnames)

# Criar uma página
book.create_sheet('Frutas')

# selecionar uma pagina 
frutas_page = book ['Frutas']
frutas_page.append(['Frutas','Quantidade','Preço'])
frutas_page.append(['Banana','5','R$ 3,90'])
frutas_page.append(['Fruta','2','R$ 3,90'])
frutas_page.append(['pêra','10','R$ 3,90'])
frutas_page.append(['maçã','3','R$ 3,90'])

# salvar a planilha
book.save('Planilha de compras.xlsx')