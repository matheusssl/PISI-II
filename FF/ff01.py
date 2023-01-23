#
import math
from itertools import permutations

Entregas = []
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


for EntregaPerm in permutations(Entregas):
    ComecoF = Distancia(PontoDePartida, EntregaPerm[0])
    FComeco = Distancia(PontoDePartida, EntregaPerm[-1])
    DistTotal = ComecoF + FComeco + \
        sum(Distancia(EntregaPerm[i], EntregaPerm[i + 1])
            for i in range(len(EntregaPerm) - 1))
    if DistTotal < DistMin:
        DistMin = DistTotal
        RotaOtima = EntregaPerm

print(*[i[2] for i in RotaOtima])
#
