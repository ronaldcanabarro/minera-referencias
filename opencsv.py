import csv
import os

with open(os.getcwd() + '\\ARQUIVOS\\' + "AFONSO_Ana_Paula_Jardim_Martins-Dissertacao2016PDF.csv", newline='', encoding='utf-8') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print(', '.join(row))