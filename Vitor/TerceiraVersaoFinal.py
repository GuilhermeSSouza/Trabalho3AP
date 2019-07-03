import cv2
import pickle 
def calcula(localImagem):
    res = cv2.imread(localImagem)
    pv = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
    ph = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]  # ph

    y = len(res)
    x = len(res[0])
    mp = [[[0]] * x] * y

    sumPH = 0  # variavel para somatorio de bordas horizontais
    sumPV = 0  # variavel para somatorio de bordas verticais
    sumRed = 0
    sumGreen = 0
    sumBlue = 0

    for i in range(1, len(res) - 1):
        for j in range(1, len(res[i]) - 1):
            accPH = 0
            accPV = 0
            for k in range(-1, 2):
                for o in range(-1, 2):
                    accPH += int(ph[k + 1][o + 1] * res[i + k][j + o][0])  # Bordas horizontais
                    accPV += int(pv[k + 1][o + 1] * res[i + k][j + o][0])  # Bordas verticais
            sumRed += res[i][j][0]  # Somatorio de vermelho
            sumGreen += res[i][j][1]  # Somatorio de verde
            sumBlue += res[i][j][2]  # Somatorio de azul
            sumPH += abs(accPH)
            sumPV += abs(accPV)
    totalPixelMenos2 = ((y - 2) * (x - 2))  # -2 pois não é pego o primeiro e último número
    resultPH = sumPH / totalPixelMenos2
    resultPV = sumPV / totalPixelMenos2
    resultRed = (sumRed / 255) / (x * y)
    resultGreen = (sumGreen / 255) / (x * y)
    resultBlue = (sumBlue / 255) / (x * y)
    result = [resultPH, resultPV, resultRed, resultGreen, resultBlue]
    return result

def img():
    resultFinal = [] #[[[0]] * 6] * 6
    listImagens = []
    for i in range(1, 5):
        for j in range(1,3): #aqui que define quantas imagens de cada pasta vão ser analisadas, nesse caso apenas 2, o professor pediu
            local = 'Images/Images' + str(i) + '/images(' + str(j) + ')'
            #print("Local: " + str(local))
            resultFinal.append(calcula(local))
            listImagens.append('Images' + str(i) + '('+str(j)+ ')')
            #print('resultadoParcial: ' + str(resultFinal[i][j]))
            #print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
        #print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        #print('checkpoint: ' + str(i))
        #print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')
    return resultFinal, listImagens 

# valores = img()
# pickle_out = open('dados.pickle', 'wb')
# pickle.dump(valores, pickle_out)
# pickle_out.close()


#print(valores)

