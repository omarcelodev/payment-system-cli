import csv
from datetime import datetime
import os

FILE_NAME = "sales_report.csv" # Nome do arquivo onde as vendas serão registradas
HEADERS = ["data", "forma_pagamento", "valor_original", "valor_final"] # Cabeçalho Padrão CSV

def save_sale(payment_name, original_value, final_value): # Registrar vendas em um arquivo CSV
    file_exists = os.path.isfile(FILE_NAME) # Verifica se o arquivo já existe

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file: # Abre o arquivo
        writer = csv.DictWriter(file, fieldnames=HEADERS) #Cria um escritor CSV baseado em dicionário

        if not file_exists: # Esreve o cabeçalho apenas se o arquivo for novo
            writer.writeheader()


        writer.writerow({ # Registra uma nova venda no CSV
            "data": datetime.now().strftime("%Y-%m-%d"), # Define a data
            "forma_pagamento": payment_name, # Informa a forma de pagamento
            "valor_original": original_value, # Informa o valor original
            "valor_final": final_value  # Informal o valor final com desconto ou juros
        })