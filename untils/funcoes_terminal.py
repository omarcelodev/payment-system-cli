import os

# Função para limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para pausar a execução
def pause(msg = "Pressione ENTER para continuar..."):
    input(msg)