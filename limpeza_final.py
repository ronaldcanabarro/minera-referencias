def retira_pontos(lista_referencias):
    lista_referencias_filtro_pontos_final = []

    lista_univer = ['UFPA','FUFPI','UFC','UFPE','UFBA','UFES','UFRJ',
            'UFRJ','UFF','UERJ','PUC-RIO','FIOCRUZ','FGV/RJ','UFMG',
            'UFJF','UFU','USP','USP','UNICAMP','UNESP-ASSIS','UNESP-FR',
            'PUC/SP','UFPR','UEM','UFSC','UFRGS','PUC/RS','UNISINOS',
            'FUPF','UFMT','UFG','UNB','UFRN','UFPB-JP','UFAM','UNIOESTE',
            'UERJ','UNIVERSO','UNEB','UFRPE','FGV/RJ','PUC-GOIÁS','UDESC',
            'UEL','UFGD','UFCG','UFOP','UNIRIO','UECE','UEFS','UFRRJ','UFSJ',
            'UFPEL','UFMA','UFSM','UNIMONTES','UNICENTRO','UNIFESP','FUFSE',
            'FURG','UEPG','UFAL','UCS','UEMA','UFG','UFRB','UFV','UNIFAL',
            'UNEB','UFFS','UNESCO', 'UFS']

    for referencia in lista_referencias:
        ok = False
        try:
            while ok != True:
                if ':' in ' '.join(referencia[2].split(' ')[:-1]) or ":" in referencia[2].split(' ')[-1]: 
                    referencia[2] = referencia[2].split(' ')
                    referencia[2].pop(-1)
                    referencia[2] = ' '.join(referencia[2])                 
                elif referencia[2].split(' ')[-1] == referencia[2].split(' ')[-1].capitalize() and referencia[2].split(' ')[-2] == referencia[2].split(' ')[-2].capitalize() and '.' not in referencia[2].split(' ')[-1] and '.' not in referencia[2].split(' ')[-2]:              
                    ok = True
                    pass 
                elif ";" in referencia[2].split(' ')[-1] or "." in referencia[2].split(' ')[-1] or "," in referencia[2].split(' ')[-1]:
                    ok = True
                    pass
                elif referencia[2].split(' ')[-1] == referencia[2].split(' ')[-1].capitalize() and referencia[2].split(' ')[-2] == referencia[2].split(' ')[-2].upper() and ',' in referencia[2].split(' ')[-2]:
                    ok = True
                    pass                
                else:
                    referencia[2] = referencia[2].split(' ')
                    referencia[2].pop(-1)
                    referencia[2] = ' '.join(referencia[2])
            
            if referencia[2].split(' ')[0] in [x+'.' for x in lista_univer] or referencia[2].split(' ')[0] in [x+',' for x in lista_univer]:
                pass
            else:
                referencia[2] = referencia[2]
                lista_referencias_filtro_pontos_final.append(referencia)
        except:
            pass

    return lista_referencias_filtro_pontos_final
