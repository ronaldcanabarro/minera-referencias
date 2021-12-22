import csv

def criar_csv(path, lista_, extensao):

    lista_referencias = []
    for refer in range(0,len(lista_)):
        lista_[refer]
        lista_referencias.append([lista_[refer][0], lista_[refer][2], lista_[refer][1]])
        
    with open(path[:len(path) - 4] + extensao + '.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f,delimiter=";")
        writer.writerow(['Source', 'Target', 'Year'])
        writer.writerows(lista_referencias)

# import xlsxwriter

# def criar_excel(path, lista_referencias, extensao):

#     row = 0
#     col = 0

#     workbook = xlsxwriter.Workbook(path[:len(path) - 4] + extensao + '.xlsx')
#     worksheet = workbook.add_worksheet()

#     worksheet.write(row, 0, 'Autor')
#     worksheet.write(row, 1, 'Citação')
#     worksheet.write(row, 2, 'Ano')

#     for autor, citacao, ano in (lista_referencias):
#         worksheet.write(row, col, autor)
#         worksheet.write(row, col + 1, citacao)
#         worksheet.write(row, col + 2, ano)
#         row += 1

#     workbook.close()