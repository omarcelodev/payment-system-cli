# Imprime separador
def print_separator():
    print("=" * 40)

# Imprime o valor formatado para moeda BRL(real)
def format_currency(value):
    return f"R$ {value:,.2f}".replace("," , "X").replace(".", ",").replace("X", ".")

# Imprime mensagem de erro
def show_error(message):
    print()
    print("⚠ ERRO")
    print(message)
    print()
    print_separator()

# Imprime o menu de opções de pagamentos
def print_menu():
    print_separator()
    print("              PAGAMENTOS")
    print_separator()
    print()
    
    print("[1] Pix        (5% de desconto)")
    print("[2] Crédito    (10% de juros)")
    print("[3] Débito     (0% desconto)")
    print("[4] Boleto     (2% de desconto)")
    print("[5] Dinheiro   (15% de desconto)")
    print()
    print("[0] Sair")
    print_separator()

# Imprime o Resumo final da compra
def show_purchase_summary(payment_name, original_value, final_value):
    difference = original_value - final_value

    print_separator()
    print("        RESUMO DA COMPRA")
    print_separator()
    print()

    print(f"Forma de pagamento : {payment_name}")
    print(f"Valor da Compra    : {format_currency(original_value)}")
    if difference > 0:
        print(f"Valor do Desconto  : {format_currency(difference)}")
    elif difference < 0:
        print(f"Valor de juros     : {format_currency(difference)} ")
    print(f"Valor Final        : {format_currency(final_value)}")
    print()

# Imprime a confirmação do pagamento
def show_confirm_payment():
    print()
    print_separator()
    print("✔ Pagamento processado com sucesso")
    print_separator()
    print()