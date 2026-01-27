from untils.funcoes_terminal import clear, pause
from untils.input import get_option, get_value
from untils.ui import print_menu
from payments import Pix, Card, Boleto

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
        if chose is None: #Se a opção não for um número, avisa o usuário
            pause()
            continue
        
        if chose == 0: #Se o usuário escolher 0, sai do loop e encerra o programa
            break

        payment_class = payment_methods.get(chose) #Pega a classe de pagamento do dicionário

        if not payment_class: #Se a classe não existir, avisa o usuário
            print("Opção Inválida")
            pause()
            continue

        value = get_value(chose) #Pega o valor correto digitado pelo usuário
        payment = payment_class(value) #Cria o objeto da classe de pagamento escolhida

        clear()
        print(f"=== RESUMO DA COMPRA ===")
        print(f"Forma de pagamento: {payment_class.__name__}")
        print(f"Valor da Compra: R${value:.2f}")
        print(f"Valor Final: R${payment.calcular_total():.2f}") #Chama o método pagar do objeto criado
        pause()

main()