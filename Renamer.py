import PyPDF2
import re
import os

pdfEspelho = "Seu espelho"
pdfBol = "Seu boleto"
def extrair_textoPdf(pdf):
    text = ""
    with open(pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

def formatar_cnpj(cnpj):
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"

def extrairValorBol(text):

    pattern = r'Valor do Documento\n(\d{1,3}(?:\.\d{3})*,\d{2})'

    money_values = re.findall(pattern, text)

    return money_values

def extrairValorEspelho(text):

    pattern = r'Valor:  (\d{1,3}(?:\.\d{3})*,\d{2})'

    money_values = re.findall(pattern, text)

    return money_values

def extrairCpf(text):
    pattern_cpf = r'\.\d{3}\.\b\d{3}\d{3}-\d{2}\b'
    cpfs = re.findall(pattern_cpf, text)

    return cpfs

def extrairCnpj(text):
     pattern_cnpj = r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b'
     cnpjs = re.findall(pattern_cnpj, text)

     return cnpjs[:2]

def extrairCnpj1(text):# O cnpj abaixo precisa ser formatado!
    pattern_cnpj1 = r'\b\d{2}\d{3}\d{3}\d{4}\d{2}\b'
    cnpjs1 = re.findall(pattern_cnpj1, text)

    cnpjs1 = [formatar_cnpj(cnpj) for cnpj in cnpjs1]
    return cnpjs1





padrao = r"-d"

for cpnjC in extrairCnpj1(extrair_textoPdf(pdfEspelho)):
    for cnpjB in extrairCnpj(extrair_textoPdf(pdfBol)):
        if (cpnjC == cnpjB):
            bol = pdfBol
            print("sim")
            for valorEsperlho in extrairValorEspelho(extrair_textoPdf(pdfEspelho)):
                for valorbol in extrairValorBol(extrair_textoPdf(pdfBol)):
                    if(valorbol == valorEsperlho):
                        print("Truee")
                        bolFormatado = re.sub(padrao,"",bol)
                        cpnjC = os.rename(pdfEspelho, "DOC-"+bolFormatado)
                    else:
                        print("não tem valor igual")
        else:
            print("Nao tem cnpj igual")
