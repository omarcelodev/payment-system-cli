from untils.funcoes_terminal import clear, pause

#Classe base para os métodos de pagamento
class Payment():
    def __init__(self, value): # Construtor que recebe o valor da compra
        self.value = value

    def calcular_total(self): # Método genérico que será sobrescrito pelas classes filhas
        return self.value

class Pix(Payment): 
    def calcular_total(self):
        return self.value * 0.95 #5% de desconto

class Card(Payment):
    def calcular_total(self):
        return self.value * 1.10 #10% de juros

class Boleto(Payment):
    def calcular_total(self):
        return self.value * 0.97 #3% de desconto

#Dicionário para mapear as opções do usuário para as classes de pagamento
payment_methods = {
    1: Pix,
    2: Card,
    3: Boleto
}

#Função garante que o usuário digite um número // O programa não quebra
def get_option():
    try:
        chose = int(input("Escolha a forma de pagamento: "))
    except ValueError:
        print("Opção inválida")
        return None
    return chose

#Função para garantir que o usuário não digite strings ou valores negativos/zero
def get_correct_value():
    try:  # Garante que o valor seja um número flaot postivo e não quebre o programa
        value = float(input("Valor da compra: R$"))
        if value <= 0.0:
            raise ValueError
        return value # Retorna o valor correto
    
    except ValueError:
        print("Valor Inválido")
        return None

#Função para retornar o valor digitado pelo usuário // com a formatação correta no terminal
def get_value(chose): # Argumento apenas para garantir a formatação correta no terminal
    while True: 
        clear()
        print_menu()
        print(f"Escolha a forma de pagamento: {chose} ") #Apenas para manter a formatação correta no terminal
        
        value = get_correct_value() #Pega o valor digitado pelo usuário
        if value is None: #Se o valor for inválido, retorna para o início do loop
            pause()
            continue
        break

    return value #Retorna o valor correto digitado pelo usuário

#Imprime o menu de opções de pagamentos
def print_menu():
    print("=== PAGAMENTOS ===")
    print("(1) Pix")
    print("(2) Cartão")
    print("(3) Boleto")
    print("(0) Sair")

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



#Detalhes: Formatar o impressão dos valores finais