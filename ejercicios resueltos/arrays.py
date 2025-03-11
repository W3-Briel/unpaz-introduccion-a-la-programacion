# vector es una array de solo un argumento(parametro) 1D. array[index]
    # [1,2,3,4]
# a partir de dos argumentos, ya se considera Matris. 2D. array[fila,columna]
    # [ [1,2,3],[4,5,6] ] 
# en una matris de 3 argumentos. 3D, array[fila,columna,profundidad]
    # [1,2,3] , [4,5,6] , [7,8,9] ]
# para crear un array, lo almacenado tiene que ser todo del mismo tipo de dato.

import array as arr
import random

# i(significa que es un entero) es el nombre del parametro
# d (es un flotante)

    # directamente lo convierte a flotante.
    # num2 = arr.array("d", [12,23])
    # print(num2[0])

# se define el tipo de dato con la letras anteriores.
    # num[0] = 1
# num = arr.array("i",[1,2,3,4,5,6])

# declarando vector vacio
    # num1 = arr.array("i", [])

# vector= arr.array('i',[])

# print(vector)

    # num4=arr.array('i',range(50,71,1))

    # for i in num4:
    #     # print(i) i toma cada valor del vector
    #     if i == 65:
    #         print(i)

    # for i in range(len(num4)):
        
    #     if num4[i] == 65:
    #         print ("index: ", i, "valor: ",num4[i])

    # for i in range(len(num4)):
    #     enumerado = list(enumerate(num4))
    #     if enumerado[i][1] == 65:
    #         print(f"el index es {enumerado[i][0]}, y el valor es {enumerado[i][1]}")

    # num5 = arr.array ('i',range (73,173,1))
    # pos1= 0
    # pos2= 0

    # for pos, i in enumerate(num5):
    #     if i == 90:
    #         pos1 = pos
    #     elif i == 106:
    #         pos2 =pos
    # print(num5[pos1:pos2])

# las matrices son mutables

    # num5[5] = 100
    # print(num5)

# num6 = arr.array('i',range(25,35,1))
# print(num6)
# num6.remove(25)
# print(num6)

# num6 = arr.array('i',range(25,35,1))
# print(num6)
# num6.pop(6)
# print(num6)