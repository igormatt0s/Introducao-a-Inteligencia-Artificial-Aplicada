'''
Implementando Jogo da Velha com Minimax

Implemente o Algoritmo Minimax para um jogo da Velha, onde o computador maximiza suas jogadas e tenta minimizar a do adversário.

Recursos importantes:
- função all()
- função max()
- função min()
- lists comprehesions
'''
# Criar tabuleiro vazio com 9 posições
tabuleiro = [' ' for _ in range(9)] # lista com 9 espaços vazios

def exibir_tabuleiro():
    for i in range(3):
        print(f"{tabuleiro[i * 3]} | {tabuleiro[i * 3 + 1]} | {tabuleiro[i * 3 + 2]}") # imprimir linhas do tabuleiro no formato 3x3
        if i < 2:
            print('---------')

def verificar_vencedor(tabuleiro, jogador):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # colunas
        [0, 4, 8], [2, 4, 6] # diagonais
    ]

    for combinacao in combinacoes_vencedoras:
        # Se todas as posições da combinação forem iguais ao jogador
        if all(tabuleiro[posicao] == jogador for posicao in combinacao):
            return True
    return False

def verificar_empate(tabuleiro):
    return " " not in tabuleiro

def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vencedor(tabuleiro, "X"):
        return -10 + profundidade
    if verificar_vencedor(tabuleiro, "O"):
        return 10 - profundidade
    if verificar_empate(tabuleiro):
        return 0

    # Testa as jogadas 
    if maximizando: # Maximiza a jogada do computador
        melhor_valor = -float('inf') # Menor valor possível
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                valor = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = " "
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else: # Testa a minimização da jogada do adversario
        melhor_valor = float('inf') # Maior valor possível
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "X"
                valor = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = " "
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor

def melhor_jogada(tabuleiro):
    melhor_valor = -float('inf') # menor valor possível
    melhor_posicao = -1

    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            valor = minimax(tabuleiro, 0, False)
            tabuleiro[i] = " "

            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i

    return melhor_posicao

def jogar_jogo():
    while True:
        exibir_tabuleiro()

        # Turno do jogador (X)
        while True:
            try:
                posicao = int(input("Escolha uma posição entre 0 - 8: "))
                if 0 <= posicao <= 8 and tabuleiro[posicao] == ' ':
                    break
                else:
                    print("Posição inválida ou ocupada! Tente novamente.")
            except ValueError:
                print("Por favor, indique um número entre 0 e 8.")
        tabuleiro[posicao] = "X"

        if verificar_vencedor(tabuleiro, "X"):
            exibir_tabuleiro()
            print("Você venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Empate!")
            break

        # Turno do computador (O)
        print("Computador está pensando...")
        melhor_posicao = melhor_jogada(tabuleiro)
        tabuleiro[melhor_posicao] = "O"

        if verificar_vencedor(tabuleiro, "O"):
            exibir_tabuleiro()
            print("O computador venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Empate!")
            break

if __name__ == "__main__":
    print("Bem vindo ao Jogo da Velha!")
    print("Você é X e o Computador é O")
    print("Posições:\n0 | 1 | 2")
    print('---------\n3 | 4 | 5')
    print('---------\n6 | 7 | 8')
    print()
    jogar_jogo()