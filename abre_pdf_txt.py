import PyPDF2

def ler_pdf(path):

    arq_pdf=open(path,'rb')
    pdf=PyPDF2.PdfFileReader(arq_pdf)
    x=pdf.numPages
    texto=[]

    for i in range(0,x):
        texto.append(pdf.getPage(i).extractText())

    texto = '\n'.join(texto)

    return texto

def ler_txt(path):

    with open(path, encoding='utf-8') as f:
        linhas = f.read()
        
    return linhas