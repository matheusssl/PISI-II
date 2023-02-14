import matplotlib.pyplot as plt

Pontos = Dados.values()
x, y = zip(*Pontos)
plt.plot(x, y, 'o-')
plt.title('Percursos')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.show()
