def print_separator():
    print("=" * 40)

# Imprime o menu de opções de pagamentos
def print_menu():
    print_separator()
    print("              PAGAMENTOS")
    print_separator()
    print()
    print("[1] Pix        (5% de desconto)")
    print("[2] Cartão     (10% de juros)")
    print("[3] Boleto     (3% de desconto)")
    print()
    print("[0] Sair")
    print_separator()

def format_currency(value):
    return f"R$ {value:,.2f}".replace("," , "X").replace(".", ",").replace("X", ".")

# Exibe mensagem de erro
def error_message():
    print("Opção inválida. Tente novamente.")

# Exibe o Resumo final da compra
def show_purchase_summary(payment_name, original_value, final_value):
    print_separator()
    print("        RESUMO DA COMPRA")
    print_separator()
    print()
    print(f"Forma de pagamento : {payment_name}")
    print(f"Valor da Compra    : {format_currency(original_value)}")
    print(f"Valor Final        : {format_currency(final_value)}")
    print()
    print_separator()
    print("✔ Pagamento processado com sucesso")
    print_separator()