from stochastic_hill_climbing import *
import numpy as np
resultados = []

for i in range(50):
    solucoes, colisoes = elevacao_estocastica()
    resultados.append((solucoes, colisoes))

iteracoes = [colisao[1] for colisao in resultados]
media = np.mean(iteracoes)
desvio_padrao = np.std(iteracoes)

print(f"Média de iterações: {media}")
print(f"Média de iterações: {media}")
print(f"Desvio padrão de iterações: {desvio_padrao}")

