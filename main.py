from payments import Pix, Card, Boleto
from untils.funcoes_terminal import clear, pause
from untils.input import get_option, get_value
from untils.ui import print_menu, show_purchase_summary, error_message

#Dicionário para mapear as opções do usuário para as classes de pagamento
payment_methods = {
    1: Pix,
    2: Card,
    3: Boleto
}
# Controla o fluxo do programa
def main():
    while True:
        clear()
        print_menu()
        
        chose = get_option()
        if chose is None:
            pause()
            continue
        
        if chose == 0:
            break
        
        payment_class = payment_methods.get(chose)
        if not payment_class:
            error_message()
            pause()
            continue

        value = get_value()
        if value is None:
            pause()
            continue

        payment = payment_class(value)

        clear

        show_purchase_summary(payment_class.__name__, value, payment.final)
        pause()
main()