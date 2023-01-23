#
import math
import random

Entregas = []
PontoDePartida = None
DistMin = math.inf

with open('FF\matriz.txt') as MatrizArq:
    for LinhaI, linha in enumerate(MatrizArq):
        Elementos = linha.split()
        for ColunaI, Elemento in enumerate(Elementos):
            if Elemento != '0':
                if Elemento == 'R':
                    PontoDePartida = (LinhaI, ColunaI, Elemento)
                else:
                    Entregas.append((LinhaI, ColunaI, Elemento))


def Distancia(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def CalcularDistTotal(Rota):
    ComecoF = Distancia(PontoDePartida, Rota[0])
    FComeco = Distancia(PontoDePartida, Rota[-1])
    return ComecoF + FComeco + sum(Distancia(Rota[i], Rota[i + 1]) for i in range(len(Rota) - 1))


def GerarPopInicial(TamanhoPop, entregas):
    Populacao = []
    for i in range(TamanhoPop):
        random.shuffle(entregas)
        Populacao.append(entregas[:])
    return Populacao


def Selecao(Populacao, fitness_fn):
    fitness = [fitness_fn(ind) for ind in Populacao]
    Probabilidade = [f/sum(fitness) for f in fitness]
    Selecionados = random.choices(Populacao, Probabilidade, k=2)
    return Selecionados


def CrossOver(pais):
    PontoCorte = random.randint(1, len(pais[0]) - 1)
    Filho1 = pais[0][:PontoCorte] + pais[1][PontoCorte:]
    Filho2 = pais[1][:PontoCorte] + pais[0][PontoCorte:]
    return (Filho1, Filho2)


def Mutacao(Individuo, ProbMutacao):
    for i, gene in enumerate(Individuo):
        if random.random() < ProbMutacao:
            Individuo[i] = random.choice(Entregas)
    return Individuo


Populacao = GerarPopInicial(100, Entregas)

for Geracao in range(100):
    NovaPop = []
    for i in range(len(Populacao)//2):
        pais = Selecao(Populacao, CalcularDistTotal)
        Filhos = CrossOver(pais)
        Filhos = [Mutacao(f, 0.01) for f in Filhos]
        NovaPop.extend(Filhos)
        Populacao = NovaPop

MelhorInd = min(Populacao, key=CalcularDistTotal)
if CalcularDistTotal(MelhorInd) < DistMin:
    DistMin = CalcularDistTotal(MelhorInd)

RotaOtima = MelhorInd
print(*[i[2] for i in RotaOtima])
#
