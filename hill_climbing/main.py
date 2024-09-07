from stochastic_hill_climbing import *
import numpy as np
from time import time


resultados = []
tempos_execucao = []

for i in range(50):
    inicio = time()
    solucoes, colisoes, iteracoes = elevacao_estocastica()
    fim = time()
    tempo_execucao = fim - inicio
    resultados.append((solucoes, colisoes, iteracoes))
    tempos_execucao.append(tempo_execucao)

iteracoes = [resultado[2] for resultado in resultados]
print(iteracoes)
media_iteracoes = np.mean(iteracoes)
desvio_padrao_iteracoes = np.std(iteracoes)

media_tempo_execucao = np.mean(tempos_execucao)
desvio_padrao_tempo_execucao = np.std(tempos_execucao)

resultados.sort(key=lambda x: x[1])
melhores_solucoes = []
melhores_unicas = set()

for resultado in resultados:
    solucao_str = str(resultado[0])
    if solucao_str not in melhores_unicas:
        melhores_solucoes.append(resultado)
        melhores_unicas.add(solucao_str)
    if len(melhores_solucoes) >= 5:
        break

print(f"Média de iterações: {media_iteracoes}")
print(f"Desvio padrão de iterações: {desvio_padrao_iteracoes}")
print(f"Média de tempo de execução: {media_tempo_execucao:.4f} segundos")
print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo_execucao:.4f} segundos")
print("\nCinco melhores soluções distintas encontradas:")
for i, (solucoes, colisoes, iteracoes) in enumerate(melhores_solucoes, start=1):
    print(f"Solução {i}: Tabuleiro = {solucoes}, Colisões = {colisoes}, Iterações = {iteracoes}")