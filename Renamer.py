import PyPDF2
import re
import os
from tkinter import filedialog, Tk, messagebox

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

def extrairCpf1(text):
    pattern_cpf = r'\d{3}\b\d{3}\d{3}\d{2}\b'
    cpfs = re.findall(pattern_cpf, text)
    cpfs = [formatar_cnpj(cpf) for cpf in cpfs]
    return cpfs

def extrairCnpj(text):
    pattern_cnpj = r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b'
    cnpjs = re.findall(pattern_cnpj, text)
    return cnpjs[:2]

def extrairCnpj1(text):  # O cnpj abaixo precisa ser formatado!
    pattern_cnpj1 = r'\b\d{2}\d{3}\d{3}\d{4}\d{2}\b'
    cnpjs1 = re.findall(pattern_cnpj1, text)
    cnpjs1 = [formatar_cnpj(cnpj) for cnpj in cnpjs1]
    return cnpjs1

tela = Tk()
tela.withdraw()

pdfEspelhos = filedialog.askopenfilenames(title="Escolha os espelhos", filetypes=[("PDF files", "*.pdf")])
pdfBoletos = filedialog.askopenfilenames(title="Escolha os boletos", filetypes=[("PDF files", "*.pdf")])

padrao = re.compile(r"-(d|D|a|A)")

if pdfEspelhos and pdfBoletos:
    for pdfEspelho in pdfEspelhos:
        cpnjsC = extrairCnpj1(extrair_textoPdf(pdfEspelho))
        cpfC= extrairCpf1(extrair_textoPdf(pdfEspelho))
        valoresEspelho = extrairValorEspelho(extrair_textoPdf(pdfEspelho))
        
        for pdfBol in pdfBoletos:
            cnpjsB = extrairCnpj(extrair_textoPdf(pdfBol))
            cpfB = extrairCpf(extrair_textoPdf(pdfBol))
            valoresBol = extrairValorBol(extrair_textoPdf(pdfBol))
            
            if set(cpnjsC).intersection(cnpjsB) or set(cpfC).intersection(cpfB):
                for valorEspelho in valoresEspelho:
                    if valorEspelho in valoresBol:
                        bolFormatado = re.sub(padrao, "", os.path.basename(pdfBol))
                        novo_nome = f"DOC-{bolFormatado}"
                        novo_caminho = os.path.join(os.path.dirname(pdfEspelho), novo_nome)
                        
                        # Se o arquivo já existir, pula para o próximo boleto
                        if os.path.exists(novo_caminho):
                            print(f"Arquivo {novo_caminho} já existe. Pulando para o próximo.")
                            continue
                        
                        # Verifica se o arquivo de origem existe antes de renomear
                        if os.path.exists(pdfEspelho):
                            os.rename(pdfEspelho, novo_caminho)
                        else:
                            print(f"Arquivo de origem {pdfEspelho} não encontrado. Pulando para o próximo.")
                        break

    messagebox.showinfo(title="FIM", message="Processo Finalizado!!!")
else:
    messagebox.showerror(title="Erro", message="Seleção de arquivos cancelada.")
