import os

from abre_pdf_txt import *
from filtros import *
from limpeza_final import *
from salva_csv_xlsx import *

"""
Busca todos os arquivos presentes na pasta 'pdfs' e filtra apenas os que tiverem 
como extensão '.pdf', '.PDF', '.txt' ou '.TXT'
"""
arquivos = os.listdir(os.getcwd() + '/ARQUIVOS/')
arquivos_pdf_txt = [arq for arq in arquivos if arq[-4:] in ['.pdf', '.PDF', '.txt', '.TXT']]

for arquivo in arquivos_pdf_txt:

    path = os.getcwd() + "\\ARQUIVOS\\" + arquivo
    print(path)
    
    try:        
        """
        Abre o arquivo de acordo com a extensão origem (pdf ou txt)
        """
        if arquivo[-3:] == 'txt' or arquivo[-3:] == 'TXT':
            texto = ler_txt(path)
        else:
            texto = ler_pdf(path)


        """
        Primeiro filtro busca palavras chaves como 'REFERÊNCIAS','Referências', 'Bibliografia', 'BIBLIOGRAFIA'
        e usa para fragmentar o texto tendo como condicional que a ultima porção (onde devem estar as referencias)
        não deve conter a palavra 'INTRODUÇÃO' ou '.......' uma vez que estas comumente se encontram antes do referencial 
        bibliografico e não neste.
        """
        texto_pos_referencia = filtro1(texto)

        """
        Todos os valore '\n' são retirados e todos os itens vazios extraidos da lista com todas as palavras
        fazendo com que uma lista ['KARVAT,', ' ', 'Erivan', '\nCassiano', 'et', '\n\nal.'] 
        mude para ['KARVAT,', 'Erivan', 'Cassiano', 'et', 'al.']
        """

        texto_pos_referencia = texto_pos_referencia.replace('\n', ' ')
        texto_pos_referencia = repr(texto_pos_referencia).replace('\\', '').split(' ')

        while '' in texto_pos_referencia:
            texto_pos_referencia.remove('')
       
        """
        Segundo filtro busca separar os paragrafos de cada referencia tendo como condicionais que o inicio do paragrafo
        comece como o nome do autor em caixa alta seguido de virgula ex. "JOÃO," e que tenha anteriormente uma palavra com ponto
        final indicando o fim de uma linha ex. "Rio de Janeiro: Dois Pontos, 1987."
        """
        lista_referencias = filtro2(texto_pos_referencia)

        """
        Terceiro filtro separa as palavras anteriores a primeira palavra inteiramente em caixa baixa,
        primeiro valor numerico ou símbolo.
        """        
        nova_lista = filtro3(lista_referencias, arquivo)

        """
        Filtro para manter um padrão de termino no nome de cada autor apenas com o ponto final na ultima palavra
        ex ['POLLAK,', 'Michael.', 'Junior.'] mude para ['POLLAK,', 'Michael.']
        """
        lista_final = retira_pontos(nova_lista)

        """
        Salva a lista de acordo com a origem do arquivo (pdf ou txt)
        """
        if len(lista_final) < 2:
            pass
        else:
            if arquivo[-3:] == 'txt' or arquivo[-3:] == 'TXT':
                criar_csv(path, lista_final, 'TXT')
            else:
                criar_csv(path, lista_final, 'PDF')

    except:
        pass
