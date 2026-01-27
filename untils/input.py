#Função garante que o usuário digite um número // O programa não quebra
def get_option():
    try:
        chose = int(input("Escolha a forma de pagamento: "))
    except ValueError:
        print("Opção inválida")
        return None
    return chose



#Função para garantir que o usuário não digite strings ou valores negativos/zero
def get_value():
    try:  # Garante que o valor seja um número flaot postivo e não quebre o programa
        value = float(input("Valor da compra: R$"))
        if value <= 0.0:
            raise ValueError
        return value # Retorna o valor correto
    
    except ValueError: # Garante que o usuário digite números
        print("Valor Inválido")
        return None