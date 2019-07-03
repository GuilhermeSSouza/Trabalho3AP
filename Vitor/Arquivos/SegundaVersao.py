import cv2
import pandas as pd

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
    sumVariancia = 0  # Esse somatório será para calcular a variancia média entre Red, Green e Blue

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
            data = {"RGB": [res[i][j][0], res[i][j][1],
                            res[i][j][2]]}  # aqui estou adicionando os 3 valores de Red Green Blue para a serie RGB
            rgb = pd.DataFrame(data)  # mesma coisa do que encima so que agr é dataframe
            #print(rgb['RGB'].var())
            #print(rgb)
            sumVariancia += rgb.var()
            # print(sumVariancia)
            sumPH += abs(accPH)
            sumPV += abs(accPV)
    totalPixelMenos2 = ((y - 2) * (x - 2))  # -2 pois não é pego o primeiro e último número
    resultPH = sumPH / totalPixelMenos2
    resultPV = sumPV / totalPixelMenos2
    resultRed = (sumRed / 255) / (x * y)
    resultGreen = (sumGreen / 255) / (x * y)
    resultBlue = (sumBlue / 255) / (x * y)
    resultVariancia = sumVariancia / (x * y)
    result = [resultPH, resultPV, resultRed, resultGreen, resultBlue, resultVariancia]
    return result

def img():
    resultFinal = [[[0]] * 6] * 6
    for i in range(1, 5):
        for j in range(1, 3): #aqui que define quantas imagens vai pegar de cada pasta, atualmente ta 2 imagens "range(1,3)" mas o professor pediu 10 então tem que por "range(1,11)"
            local = 'Images/Images' + str(i) + '/images(' + str(j) + ')'
            print("Local: " + str(local))
            resultFinal[i][j] = calcula(local)
            print('resultadoParcial: ' + str(resultFinal[i][j]))
            print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('checkpoint: ' + str(i))
        print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')
    # para cada print vai mostrar
    # resultado bordasHorizontais, BordasVerticais, Vermelho, Verde, Azul, Variancia bugada do kct

img()