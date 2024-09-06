import random

TAMANHO_POPULACAO = 20
TAXA_CROSSOVER = 0.8
TAXA_MUTACAO = 0.03
MAXIMO_GERACOES = 1000

def criar_individuo():
    return [format(random.randint(0, 7), '03b') for _ in range(8)]

def calcular_fitness(individuo):
    colisoes = 0
    individuo_decimal = [int(gene, 2) for gene in individuo]
    for i in range(len(individuo_decimal)):
        for j in range(i + 1, len(individuo_decimal)):
            if individuo_decimal[i] == individuo_decimal[j] or abs(individuo_decimal[i] - individuo_decimal[j]) == j - i:
                colisoes += 1
    return colisoes

def selecao_roleta(populacao):
    max_fitness = sum([calcular_fitness(ind) for ind in populacao])
    escolha = random.uniform(0, max_fitness)
    atual = 0
    for ind in populacao:
        atual += calcular_fitness(ind)
        if atual > escolha:
            return ind

def crossover(pai1, pai2):
    if random.random() < TAXA_CROSSOVER:
        ponto = random.randint(1, len(pai1) - 1)
        return pai1[:ponto] + pai2[ponto:], pai2[:ponto] + pai1[ponto:]
    return pai1, pai2

def mutacao(individuo):
    if random.random() < TAXA_MUTACAO:
        ponto = random.randint(0, len(individuo) - 1)
        individuo[ponto] = format(random.randint(0, 7), '03b')
    return individuo

def algoritmo_genetico():
    populacao = [criar_individuo() for _ in range(TAMANHO_POPULACAO)]
    for geracao in range(MAXIMO_GERACOES):
        populacao = sorted(populacao, key=lambda x: calcular_fitness(x))
        if calcular_fitness(populacao[0]) == 0:
            break
        nova_populacao = populacao[:2]  # Elitismo
        while len(nova_populacao) < TAMANHO_POPULACAO:
            pai1 = selecao_roleta(populacao)
            pai2 = selecao_roleta(populacao)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.append(mutacao(filho1))
            nova_populacao.append(mutacao(filho2))
        populacao = nova_populacao[:TAMANHO_POPULACAO]
        print(populacao)
    colisao = calcular_fitness(populacao[0])
    return populacao[0], geracao, colisao
