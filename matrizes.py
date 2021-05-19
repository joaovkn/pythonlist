import pandas as pd
import numpy as np
from scipy import spatial


matriz = pd.read_csv(r'ml-100k.csv', header = None ,delim_whitespace=True)

matriz = matriz.to_numpy()  
matrizn = np.copy(matriz)
matrizn[matrizn == 0] = np.nan

# Lendo a batata
# print("Batata:\nTipo:", matrizn.dtype,"\n", matrizn)

#Resoluções:

#1
media = np.nanmean(matrizn)
desviopadrao = np.nanstd(matrizn)
variancia = np.nanvar(matrizn)
print("Média da matriz:", media)
print("Desvio padrão da matriz:", desviopadrao)
print("Variância da matriz:", variancia)

#2
totaluser = len(matrizn)
matriz2 = np.zeros((943,3))
for x in range(totaluser):
    matriz2[x][0] = np.nanmean(matrizn[x])
    matriz2[x][1] = np.nanstd(matrizn[x])
    matriz2[x][2] = np.nanvar(matrizn[x])
    print("Usuário:", x)
    print("Média:", "{:.2f}".format(matriz2[x][0]))
    print("Desvio padrão:", "{:.2f}".format(matriz2[x][1]))
    print("Variância:", "{:.2f}".format(matriz2[x][2]))

#3
onoff = 1
valoresproxmedia = np.zeros(5)
usersproxmedia = np.zeros(5)
for x in range(totaluser):
    onoff = 1
    for y in range(len(valoresproxmedia)):
        diferenca =  abs(media - valoresproxmedia[y])
        diferenca2 = abs(media - matriz2[x][0])
        if((diferenca2 < diferenca) and (onoff == 1)):
            valoresproxmedia[y] = matriz2[x][0]
            usersproxmedia[y] = x
            onoff = 0
#Verificador de média
# for x in range(len(matrizn[0])):
#     if(~np.isnan(matriz[x][912])):
#         print(matriz[x][912])
print("Média da matriz:", media)
print("Usuários próximos da média:", usersproxmedia)
print("Médias próximas da média:", valoresproxmedia)

#4

#5

onoff = 1
overavaliadores = []
overavaliacoes = []
valoramais = 1.2
for x in range(totaluser):
    onoff = 1
    if(matriz2[x][0]>(media+valoramais)):
        overavaliadores.append(x)
        overavaliacoes.append(matriz2[x][0])

numpou = np.array(overavaliadores)
numpou2 = np.array(overavaliacoes)
np.sort(overavaliadores)
np.sort(overavaliacoes)

print("Usuários positivos:", np.sort(overavaliadores))
print("Médias positivas:", np.sort(overavaliacoes))


#6
print(matriz[0])
print(matriz[1])
# print(matriz[:,0])
# print(matriz[:,1])

def SimiliaridadeCos(linha1, linha2):
    result = 1 - spatial.distance.cosine(linha1, linha2)
    print("Distância por similiaridade do cosseno: ",result)

def CorrelacaoPearson(linha1, linha2):
    result2 = spatial.distance.correlation(linha1, linha2)
    print("Distancia por correlação de Pearson: ", result2)
    
#Linha teste
SimiliaridadeCos(matriz[0], matriz[1])
CorrelacaoPearson(matriz[0], matriz[1])
#Coluna teste
SimiliaridadeCos(matriz[:,1], matriz[:,0])
CorrelacaoPearson(matriz[:,1], matriz[:,0])