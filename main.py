
from maquina import Maquina


# Abrir e ler o arquivo de texto
f = open("config.txt", "r")
arquivo = f.read().splitlines()


# Tratando o arquivo

# Tratamento para o alfabeto
alfabeto = []

for letra in arquivo[0]:
    alfabeto.append(letra)


# Tratamento para os estados
nEstados = int(arquivo[1])
nTransicoes = int(arquivo[2])
estados = []

for transicao in range(3, nTransicoes + 3, 1):
    if int(arquivo[transicao][0]) > len(estados):
        estados.append([])
    
    estados[-1].append((arquivo[transicao].split(" ")))

# Tratamento de entradas
nEntradas = int(arquivo[nTransicoes + 3])
entradas = []

for entrada in range(nTransicoes+4, nTransicoes+4+nEntradas):
    entradas.append(arquivo[entrada])


mt = Maquina(alfabeto, estados)

print(mt.start(entradas))