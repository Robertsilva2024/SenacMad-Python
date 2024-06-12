import random


# Função para criar o tabuleiro
def criar_tabuleiro(tamanho):
    return [['~'] * tamanho for _ in range(tamanho)]


# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))


# Função para posicionar os navios no tabuleiro
def posicionar_navios(tabuleiro, num_navios):
    tamanho = len(tabuleiro)
    navios = []
    while len(navios) < num_navios:
        linha = random.randint(0, tamanho - 1)
        coluna = random.randint(0, tamanho - 1)
        if tabuleiro[linha][coluna] == '~':
            tabuleiro[linha][coluna] = 'N'
            navios.append((linha, coluna))
    return navios


# Função principal do jogo
def jogar_batalha_naval(tamanho=5, num_navios=3, tentativas=10):
    tabuleiro = criar_tabuleiro(tamanho)
    navios = posicionar_navios(tabuleiro, num_navios)
    acertos = 0

    print("Bem-vindo ao jogo de Batalha Naval!")
    print(f"Há {num_navios} navios escondidos no tabuleiro {tamanho}x{tamanho}.")

    for tentativa in range(tentativas):
        exibir_tabuleiro(tabuleiro)
        print(f"Tentativa {tentativa + 1} de {tentativas}")

        while True:
            try:
                linha = int(input(f"Digite a linha (0 a {tamanho - 1}): "))
                coluna = int(input(f"Digite a coluna (0 a {tamanho - 1}): "))
                if 0 <= linha < tamanho and 0 <= coluna < tamanho:
                    break
                else:
                    print("Entrada inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        if (linha, coluna) in navios:
            print("Você acertou um navio!")
            tabuleiro[linha][coluna] = 'X'
            acertos += 1
            navios.remove((linha, coluna))
        else:
            print("Você errou!")
            tabuleiro[linha][coluna] = 'O'

        if acertos == num_navios:
            print("Parabéns! Você afundou todos os navios!")
            break
    else:
        print("Fim das tentativas. Você não conseguiu afundar todos os navios.")

    print("Tabuleiro final:")
    exibir_tabuleiro(tabuleiro)


# Executar o jogo
jogar_batalha_naval()