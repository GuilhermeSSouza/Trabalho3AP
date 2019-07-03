from random import *
from math import *
#import TerceiraVersaoFinal as tvf
import pickle 



pickle_in = open('dados.pickle','rb')

X = pickle.load(pickle_in)

N = len(X)

#D = [[0.0 for i in range(N)] for j in range(N)]
D_1 = [[0.0 for i in range(N)] for j in range(N)]





def dist_euclides(a,b):
	soma = 0.0
	for i in range(len(a)):
		soma += (a[i]-b[i])**2

	return sqrt(soma)


for i in range (0,N):
	for j in range (0,N):
		D_1[i][j]=dist_euclides(X[i],X[j])


pickle_out = open('D.pickle', 'wb')
pickle.dump(D_1, pickle_out)
pickle_out.close()
