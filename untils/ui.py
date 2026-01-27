
#Imprime o menu de opções de pagamentos
def print_menu():
    print("=== PAGAMENTOS ===")
    print("(1) Pix")
    print("(2) Cartão")
    print("(3) Boleto")
    print("(0) Sair")


def error_message():
    print("Opção inválida. Tente novamente.")

def show_purchase_summary(payment_name, original_value, final_value):
    print("=== RESUMO DA COMPRA ===")
    print(f"Forma de pagamento: {payment_name}")
    print(f"Valor da Compra: R$ {original_value:.2f}")
    print(f"Valor Final: R${final_value:.2f}")
