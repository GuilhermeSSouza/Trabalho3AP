import numpy as np
from random import *
from math import *


#Distancia Euclideana
def dist_eucli(x,y):
	return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2 )


#Matriz de Dissimilaridade
def calcMatrizDissi(data):
	matriz = np.zeros((len(data),len(data)), dtype=np.float64)
	for i in range(len(data)):
		for j in range(len(data)):
			matriz[i][j]=dist_eucli(data[i],data[j])
	return matriz


def roleta(pesos):
	somaPeso = 0
	for i in range(len(pesos)):
		somaPeso += pesos[i]
	#print(pesos)
	#print(somaPeso)
	pesoSort = randint(1, int(somaPeso))#no caso uso '1' ao invés de '0' para não dar uma possibilidade a mais
	percorre = -1
	pesoAtual = 0
	indicSort = -1
	while indicSort < 0:
		percorre += 1
		pesoAtual += pesos[percorre]
		#print('PesoAtual: ' + str(pesoAtual))
		#print('pesoSort: ' + str(pesoSort))
		#print('pesos[percorre]: ' + str(percorre))
		if (pesoAtual >= pesoSort and (pesoAtual - pesos[percorre]) <= pesoSort):
			#print('<><><><><><><><><><><><><><><><><><><><><><><><>')
			#print('PesoAtual: ' + str(pesoAtual))
			#print('pesoSort: ' + str(pesoSort))
			#print('Indice Lista: ' + str(percorre))
			indicSort = percorre
	return percorre


def pesos(matrizDissiInt):
	pesos = list()
	for i in range(len(matrizDissiInt)):
		for j in range(len(matrizDissiInt[0])):
			if(i == j):
				pesos.append(-1)
			else:
				pesos.append(matrizDissiInt[i][j])
	return pesos


def converteInt(matriz):
	matrizConvertida = np.zeros((len(matriz),len(matriz)), dtype=np.int)
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			matrizConvertida[i][j] = int(matriz[i][j]*1000)#para pegar 3 digitos apos a virgula e continuar usando inteiros
	return matrizConvertida


def distanciaMedia(listaPesos):
	nItens = sqrt(len(listaPesos))
	#print(nItens)
	cont = 0
	soma = 0
	result = list()
	for i in range(len(listaPesos)):
		if(cont < nItens):
			cont+=1
			soma+= listaPesos[i]
		else:
			#print('result: '+str((soma+1)/(nItens-1)))
			result.append((soma+1)/(nItens-1))
			cont = 1
			soma = listaPesos[i]

	return result


def getPesos(data):
	matrizDissi = calcMatrizDissi(data)
	matrizDissiInt = converteInt(matrizDissi)
	return pesos(matrizDissiInt)


def iniciaDoisGrupos(data):
	g = data
	g1 = list()
	g2 = list()
	pesos = getPesos(data)
	for i in range(len(data)):
		if i%2 == 1:
			g1.append(data[i])
		else:
			g2.append(data[i])
	#print('Data: '+str(data))
	#print('G1: '+str(g1))
	#print('G2: '+str(g2))
	executa(data, g1, g2)


def executa(data, g1, g2):
	for i in range(1000):
		resultG1 = distanciaMedia(getPesos(g1))
		resultG2 = distanciaMedia(getPesos(g2))
		removidoG1 = g1.pop(roleta(resultG1))
		removidoG2 = g2.pop(roleta(resultG2))
		g1.append(removidoG2)
		g2.append(removidoG1)
		#mutação
		if(randint(0,1000)>9990):
			if(randint(0,1)==0):
				resultG1 = distanciaMedia(getPesos(g1))
				g1.append(roleta(resultG1))
			else:
				resultG2 = distanciaMedia(getPesos(g2))
				g2.append(roleta(resultG2))
	print('Dados usados: '+str(data))
	print('Grupo 1: '+str(g1))
	print('Grupo 2: '+str(g2))

data = [[0,0], [4,3],[16,9],[4,4], [16,10]]
iniciaDoisGrupos(data)