# Implementação do algortimo Backtracking com recursão:

'''
Implemente um algoritmo utilizando a técnica de Backtracking para resolver o seguinte problema:

Dado um tabuleiro NXN, marque o melhor caminho encontrado entre uma posição inicial e uma posição final. A definição do tabuleiro será feito em uma matriz que vai conter espaços vazios e espaços bloqueados (utilize um X).
'''

import sys

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(f"| {' | '.join(linha)} |")
    print("\n")

def chegou_destino(proxima_linha, proxima_coluna):
    return proxima_linha == 0 and proxima_coluna == 3

def movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
    return (
        0 <= proxima_linha < len(tabuleiro) and 
        0 <= proxima_coluna < len(tabuleiro[0]) and 
        tabuleiro[proxima_linha][proxima_coluna] != 'X' and 
        tabuleiro[proxima_linha][proxima_coluna] != '*'
    )

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade, visitados):
    if chegou_destino(linha_atual, coluna_atual):
        return linha_atual, coluna_atual, profundidade
    
    visitados.add((linha_atual, coluna_atual))
    melhor_profundidade = float('inf')
    melhor_linha, melhor_coluna = linha_atual, coluna_atual

    direcoes = [
        (0, 1),   # Direita
        (0, -1),  # Esquerda
        (-1, 0),  # Cima
        (1, 0)    # Baixo
    ]

    for d_linha, d_coluna in direcoes:
        proxima_linha = linha_atual + d_linha
        proxima_coluna = coluna_atual + d_coluna

        if movimento_valido(tabuleiro, proxima_linha, proxima_coluna) and (proxima_linha, proxima_coluna) not in visitados:            
            tabuleiro[proxima_linha][proxima_coluna] = '*'
            _, _, proxima_profundidade = proximo_movimento(tabuleiro, proxima_linha, proxima_coluna, profundidade + 1, visitados)
            tabuleiro[proxima_linha][proxima_coluna] = ' '

            if proxima_profundidade < melhor_profundidade:
                melhor_linha, melhor_coluna, melhor_profundidade = proxima_linha, proxima_coluna, proxima_profundidade

    visitados.remove((linha_atual, coluna_atual))
    return melhor_linha, melhor_coluna, melhor_profundidade

def main():
    tabuleiro = [
        ['X', ' ', ' ', ' '],
        [' ', 'X', 'X', ' '],
        [' ', ' ', ' ', ' ']
    ]
    linha_atual, coluna_atual = 2, 0
    tabuleiro[linha_atual][coluna_atual] = '*'

    mostrar_tabuleiro(tabuleiro)

    while sys.stdin.read(1) and not chegou_destino(linha_atual, coluna_atual):
        visitados = set()
        melhor_linha, melhor_coluna, melhor_profundidade = proximo_movimento(tabuleiro, linha_atual, coluna_atual, 0, visitados)

        if melhor_profundidade == float('inf'):
            print("Não foi possível encontrar caminho.")
            break

        linha_atual, coluna_atual = melhor_linha, melhor_coluna
        tabuleiro[linha_atual][coluna_atual] = '*'
        print(f"Próxima linha = {melhor_linha}, Próxima coluna = {melhor_coluna} e Profundidade = {melhor_profundidade}")
        mostrar_tabuleiro(tabuleiro)

if __name__ == "__main__":
    main()
