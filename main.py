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
        print_menu() # Impressão do Menu
        
        chose = get_option() # Coletando opção do usuário
        if chose is None:
            pause()
            continue
        
        if chose == 0:
            break
        
        payment_class = payment_methods.get(chose) # Selecionado método de pagamento correto
        if not payment_class:
            error_message()
            pause()
            continue

        value = get_value() # Coletando o valor digitado pelo usuário   
        if value is None:
            pause()
            continue

        payment = payment_class(value) # Instancia a forma de pagamento escolhida com o valor da compra

        clear()
        show_purchase_summary(payment_class.__name__, value, payment.final) # Resumo Final da compra
        pause()
main()