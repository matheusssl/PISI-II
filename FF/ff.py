import time

Arquivo = open("matriz.txt", "r")
Rotas = []
TempoInicio = time.time()

def Processar():
    Pontos = {}
    i, j = map(int, Arquivo.readline().split(" "))
    for l in range(i):
        Linhas = Arquivo.readline().split(" ")
        for Colunas in range(len(Linhas)):
            if "\n" in Linhas[Colunas]:
                Linhas[Colunas] = Linhas[Colunas][:-1]
            if Linhas[Colunas] != "0":
                Pontos[Linhas[Colunas]] = (l, Colunas)
    return Pontos

def Permutacao(Pontos, i=0):
    if i == len(Pontos):
        Rotas.append("R" + "".join(Pontos) + "R")
    for j in range(i, len(Pontos)):
        Rotas2 = [Pontos2 for Pontos2 in Pontos]
        Rotas2[i], Rotas2[j] = Rotas2[j], Rotas2[i]
        Permutacao(Rotas2, i + 1)
    return Rotas

def CustoMin(Rotas2, Pontos):
    Custo = {}
    Minimo = 10**6
    Minimo2 = str
    for r in Rotas2:
        Custo2 = 0
        for p in range(len(r) - 1):
            Custo2 += abs(Pontos[r[p + 1]][0] - Pontos[r[p]][0]) + \
                abs(Pontos[r[p + 1]][1] - Pontos[r[p]][1])
        v = [Pontos2 for Pontos2 in r[1:len(r) - 1]]
        Custo[" ".join(v)] = Custo2
    for i in Custo.items():
        k, vl = i
        if vl < Minimo:
            Minimo2 = k
            Minimo = vl
    return print(Minimo2)

Dados = Processar()
CustoMin(Permutacao([Pontos2 for Pontos2 in Dados if Pontos2 != "R"]), Dados)
TempoTotal = time.time()
print("Tempo Gasto:", TempoTotal - TempoInicio)