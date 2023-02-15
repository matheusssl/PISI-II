# importa a biblioteca de tempo
import time

# abre o arquivo de matriz.txt em modo de leitura
Arquivo = open("Flyfood\matriz.txt", "r")

# cria uma lista vazia para armazenar as rotas possíveis
Rotas = []

# define o tempo de início da execução
TempoInicio = time.time()

# define uma função para processar os pontos a partir do arquivo de entrada
def Processar():
    # cria um dicionário vazio para armazenar os pontos
    Pontos = {}
    # lê a primeira linha do arquivo que contém as dimensões da matriz
    i, j = map(int, Arquivo.readline().split(" "))
    # itera sobre as linhas da matriz
    for l in range(i):
        # lê a linha atual da matriz e divide em colunas
        Linhas = Arquivo.readline().split(" ")
        # itera sobre as colunas da linha atual
        for Colunas in range(len(Linhas)):
            # remove a quebra de linha, se houver
            if "\n" in Linhas[Colunas]:
                Linhas[Colunas] = Linhas[Colunas][:-1]
            # se o valor da célula atual for diferente de 0, adiciona o ponto ao dicionário
            if Linhas[Colunas] != "0":
                Pontos[Linhas[Colunas]] = (l, Colunas)
    # retorna o dicionário de pontos processados
    return Pontos

# define uma função para gerar todas as permutações possíveis dos pontos
def Permutacao(Pontos, i=0):
    # se chegou ao final da lista de pontos, adiciona a rota à lista de rotas
    if i == len(Pontos):
        Rotas.append("R" + "".join(Pontos) + "R")
    # itera sobre a lista de pontos a partir do índice i
    for j in range(i, len(Pontos)):
        # cria uma cópia da lista de pontos
        Rotas2 = [Pontos2 for Pontos2 in Pontos]
        # troca o ponto na posição i com o ponto na posição j
        Rotas2[i], Rotas2[j] = Rotas2[j], Rotas2[i]
        # chama a função recursivamente, incrementando i
        Permutacao(Rotas2, i + 1)
    # retorna a lista de rotas geradas
    return Rotas

# define uma função para calcular o custo mínimo de cada rota
def CustoMin(Rotas2, Pontos):
    # cria um dicionário vazio para armazenar os custos
    Custo = {}
    # define o valor mínimo como um valor grande
    Minimo = 10**6
    # define o valor mínimo de rota como uma string vazia
    Minimo2 = str
    # itera sobre as rotas geradas
    for r in Rotas2:
        # define o custo inicial como 0
        Custo2 = 0
        # itera sobre os pontos da rota
        for p in range(len(r) - 1):
            # calcula o custo entre o ponto atual e o próximo ponto na rota
            Custo2 += abs(Pontos[r[p + 1]][0] - Pontos[r[p]][0]) + abs(Pontos[r[p + 1]][1] - Pontos[r[p]][1])
        v = [Pontos2 for Pontos2 in r[1:len(r) - 1]] # cria uma nova lista de pontos sem o primeiro e último elemento e junta-os em uma única string separada por espaço
        Custo[" ".join(v)] = Custo2
    for i in Custo.items():
        k, vl = i # pega a chave e o valor da entrada do dicionário
        if vl < Minimo:
            Minimo2 = k
            Minimo = vl # se o valor for menor que Minimo, atualiza Minimo e Minimo2
    return print(Minimo2) # imprime a rota com menor custo
  
Dados = Processar() # Processa os dados do arquivo
CustoMin(Permutacao([Pontos2 for Pontos2 in Dados if Pontos2 != "R"]), Dados) # Calcula a rota de menor custo
TempoTotal = time.time() # Calcula o tempo total de execução do código
print("Tempo Gasto:", TempoTotal - TempoInicio) # Imprime o tempo total gasto na execução do código
