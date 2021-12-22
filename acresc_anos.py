# def anos_acres(lista_referencias, arq):
        
#     lista_autor_anos = []

#     for referencia in lista_referencias:
#         nome_autor = []
#         lista_anos = []

#         for itens in referencia:
#             if type(itens) == str:
#                 nome_autor.append(itens)
#             else:
#                 lista_anos.append(itens)

#         if len(nome_autor) < 2:
#             pass
#         else:
#             nome_autor = ' '.join(nome_autor)
#             for ano in lista_anos:
#                 if [arq, nome_autor, ano] in lista_autor_anos:
#                     pass
#                 else:
#                     if ';' in nome_autor:
#                         nomes = nome_autor.split(';')
#                         for nome in nomes:
#                             if [arq, nome, ano] in lista_autor_anos:
#                                 pass
#                             else:
#                                 lista_autor_anos.append([arq, nome, ano])
#                     else:
#                         lista_autor_anos.append([arq, nome_autor, ano])
    
#     return lista_autor_anos