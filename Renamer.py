import PyPDF2
import re

pdf_path = "SEU PDF 1"
pdf_path1 = "SEU PDF 2"
def extrair_textoPdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

def extrairValor(text):

    pattern = r'\d+(?:,\d+)?'

    money_values = re.findall(pattern, text)

    return money_values

def extrairCpf(text):
    pattern_cpf = r'\.\d{3}\.\b\d{3}\d{3}-\d{2}\b'
    cpfs = re.findall(pattern_cpf, text)

    return cpfs

def extrairCnpj(text):
     pattern_cnpj = r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b'
     cnpjs = re.findall(pattern_cnpj, text)

     return cnpjs

def extrairCnpj1(text):
    pattern_cnpj1 = r'\b\d{2}\d{3}\d{3}\d{4}\d{2}\b'
    cnpjs1 = re.findall(pattern_cnpj1, text)

    return cnpjs1



for cnpj in extrairCnpj(extrair_textoPdf(pdf_path)):
    print(cnpj)
for cnpj in extrairCnpj1(extrair_textoPdf(pdf_path)):
    print(cnpj)
print(extrair_textoPdf(pdf_path))
#print(extrairValor(extrair_textoPdf(pdf_path)))
#print(extrairCpf(extrair_textoPdf(pdf_path)))