import string

def filtro1(texto):
    lista_filtro = ['REFERÊNCIAS','Referências', 'Bibliografia', 'BIBLIOGRAFIA', 
                'Bibliográfica', 'REFERÊNCIAS E FONTES', 'REFERÊNCIAS BIBLIOGRÁFICAS', 
                'BIBLIOGRÁFICAS']

    for item in lista_filtro:

        texto_filtrado = texto.split(item)
        
        if len(texto_filtrado) == 1:
            pass
        else:
            texto_filtrado_pos_referencia = texto_filtrado[-1]
            if 'INTRODUÇÃO' in texto_filtrado_pos_referencia:
                pass
            elif "......." in texto_filtrado_pos_referencia:
                pass
            else:
                return texto_filtrado_pos_referencia
    

def filtro2(texto_referencias):
    
    num = len(texto_referencias)
    for i in range(0, num):
        texto_referencias[i] = texto_referencias[i].strip()
        texto_referencias[i] = texto_referencias[i].replace("”",'')
        texto_referencias[i] = texto_referencias[i].replace("“",'')
        texto_referencias[i] = texto_referencias[i].replace("‘",'')
        texto_referencias[i] = texto_referencias[i].replace("’",'')

    referencia = []
    lista_referencias = []
    lista_letras = string.ascii_uppercase + 'ÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛ'
    num = len(texto_referencias)
    for i in range(0, num):
        
        if i == len(texto_referencias) - 1 or i == len(texto_referencias) - 2:
            referencia.append(texto_referencias[i])
            pass
        else:
            if len(texto_referencias[i + 1]) > 1:
                if texto_referencias[i + 1] == texto_referencias[i + 1].upper():
                    if texto_referencias[i + 1][0] in lista_letras and texto_referencias[i + 1][1] in lista_letras or texto_referencias[i + 1][0:2] == "__":
                        if texto_referencias[i][-1] not in lista_letras:
                            referencia.append(texto_referencias[i])
                            lista_referencias.append(referencia)
                            referencia = []
                        else:
                            referencia.append(texto_referencias[i])
                    else:
                        referencia.append(texto_referencias[i])
                else:
                    referencia.append(texto_referencias[i])
            else:
                referencia.append(texto_referencias[i])
                
    return lista_referencias

def filtro3(lista_referencias, arquivo):
    nova_lista = []
    lista_anos = [str(x) for x in list(range(1900, 2025))]
    lista_num = '0123456789'
    simbolos = '*:/\\()[]}{%+'
    for paragrafo in lista_referencias:
        lista_palavras = []
        cont = 0
        for palavra in range(0, len(paragrafo)):
            lista_palavras.append(paragrafo[palavra])
            if paragrafo[palavra] == paragrafo[-1]:
                texto = ' '.join(lista_palavras).strip()
                if texto[0:2] == '__':
                    nova_lista.append(nova_lista[-1])
                else:
                    nova_lista.append([arquivo[:-8].replace("_", " "), arquivo[-8:-4], texto])
            elif paragrafo[palavra + 1] == paragrafo[palavra + 1].lower() or any([x if x in paragrafo[palavra + 1] else False for x in lista_anos]) or any([x if x in paragrafo[palavra + 1] else False for x in lista_num])  or any([x if x in paragrafo[palavra + 1] else False for x in simbolos]):
                texto = ' '.join(lista_palavras).strip()
                if texto[0:2] == '__':
                    nova_lista.append(nova_lista[-1])
                else:
                    nova_lista.append([arquivo[:-8].replace("_", " "), arquivo[-8:-4], texto])
                break
            else:
                pass
    return nova_lista