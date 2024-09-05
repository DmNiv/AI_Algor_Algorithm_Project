from random import randint
from time import sleep

def calcular_colisoes(tabuleiro):
    colisoes = 0
    for i in range(len(tabuleiro)):
        for j in range(i + 1, len(tabuleiro)):
            if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j] == abs(i - j)):
                colisoes += 1

    return colisoes

def vizinho_aleatorio(tabuleiro):
    vizinho = tabuleiro.copy()
    linha = randint(0, 7)
    coluna = randint(0, 7)
    vizinho[coluna] = linha
    return vizinho

def elevacao_estocastica():
    tabuleiro = [randint(0, 7) for i in range(8)]
    colisoes_atuais = calcular_colisoes(tabuleiro)
    iteracoes = 0
    fitness = 500
    while iteracoes < fitness:
        vizinho = vizinho_aleatorio(tabuleiro)
        colisoes_vizinho = calcular_colisoes(vizinho)
        if colisoes_vizinho < colisoes_atuais:
            tabuleiro = vizinho
            colisoes_atuais = colisoes_vizinho
            iteracoes = 0
        else:
            iteracoes += 1
        print(tabuleiro, colisoes_atuais, iteracoes)
        sleep(0.05)
    return tabuleiro, colisoes_atuais
