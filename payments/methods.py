#Classe base para os métodos de pagamento
class Payment():
    def __init__(self, value): # Construtor que recebe o valor da compra
        self.value = value
        self.final = self.calculate_final() # Guarda o valor final

    def calculate_final(self): # Método genérico que será sobrescrito pelas classes filhas
        return self.value

class Pix(Payment): 
    def calculate_final(self):
        return self.value * 0.95 #5% de desconto

class Credit_Card(Payment):
    def calculate_final(self):
        return self.value * 1.10 #10% de juros

class Debit_Card(Payment):
    def calculate_final(self):
        return self.value #0% de desconto

class Money(Payment):
    def calculate_final(self):
        return self.value * 0.85 #15% de desconto

class Boleto(Payment):
    def calculate_final(self):
        return self.value * 0.98 #2% de desconto
