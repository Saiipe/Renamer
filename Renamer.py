import PyPDF2
import re

pdf_path = "Nome do pdf"
def extrair_textoPdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

def extrair_valor(text):

    # Padrão de expressão regular para encontrar valores monetários no formato R$X.XX
    pattern = r'\d+(?:,\d+)?'

    # Encontrar todos os valores monetários no texto
    money_values = re.findall(pattern, text)

    # Retornar a lista de valores monetários encontrados
    return money_values

def extriarCpfeCnpj(text):
    # Padrão de expressão regular para encontrar CPFs e CNPJs
    pattern_cpf = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
    pattern_cnpj = r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b'
    pattern_cnpj1 = r'\b\d{2}\d{3}\d{3}\d{4}\d{2}\b'


    # Encontrar todos os CPFs e CNPJs no texto
    cpfs = re.findall(pattern_cpf, text)
    cnpjs = re.findall(pattern_cnpj, text)
    cnpjs1 = re.findall(pattern_cnpj1, text)
    # Retornar a lista de CPFs e CNPJs encontrados
    return cpfs, cnpjs, cnpjs1

#print(extrair_textoPdf(pdf_path))
print(extrair_valor(extrair_textoPdf(pdf_path)))
print(extriarCpfeCnpj(extrair_textoPdf(pdf_path)))