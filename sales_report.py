import csv
from datetime import datetime
import os

FILE_NAME = "sales_report.csv"
HEADERS = ["data", "forma_pagamento", "valor_original", "valor_final"]

def save_sale(payment_name, original_value, final_value):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)

        if not file_exists:
            writer.writeheader()


        writer.writerow({
            "data": datetime.now().strftime("%Y-%m-%d"),
            "forma_pagamento": payment_name,
            "valor_original": original_value,
            "valor_final": final_value 
        })