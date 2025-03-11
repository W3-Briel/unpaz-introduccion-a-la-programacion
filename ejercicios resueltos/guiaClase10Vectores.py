#importando librerias
import array as arr
import random as r

###################################### 63)

# Escriba un programa que contenga un vector de 10 posiciones con valores enteros mayores
# a 1000 y menores a 2000, luego muestre los valores y sus posiciones.

# vector1 = arr.array("i",[])

# if len(vector1) < 10:
#     while len(vector1) < 10:
#         numeroAleatorio = r.randint(1001,1999)
#         vector1.append(numeroAleatorio)
#     for x,y in enumerate(vector1):
#         print(f"index: {x}, y contenido: {y}\n")

# utilice numeros aleatorios sin querer(?)


###################################### 64)

# Escriba un programa que cargue un vector desde el número 100 al 200, debe utilizar 2
# métodos de carga, usando range y otro utilizando while, luego muestre los valores unos al
# lado del otro.

# Metodo con While

# vector2 = arr.array("i",[])
# valores = 100

# while valores <= 200:
#     vector2.append(valores)
#     if valores == 200:
#         print(*vector2)
#         break
#     valores += 1

# Metodo con range

# vector3 = arr.array("i",range(100,201))
# print(*vector3)

###################################### 65)

# Escriba un programa que permita cargar por teclado un vector de 10 posiciones, con
# números enteros, luego debe mostrar los números pero si el número termina en 3 8 4 9 debe
# agregar un * antes de mostrar el número (investigue cómo obtener un ultimo digito de un
# número) 

# vector4 = arr.array("i",[])

# while len(vector4) < 10:
#     valores_a_agregar = int(input("que valor deseas agregar al array??: "))
#     vector4.append(valores_a_agregar)

# for valor in vector4:
#     valor_termina_en = valor % 10
#     if valor_termina_en in (3,8,4,9):
#         print("*",valor)
#     else:
#         print(valor)

###################################### 66)

# Escriba un programa que llene un vector de 100 posiciones con números aleatorios entre
# 1990 y 2022,muestre los elementos del vector y su cantidad de elementos, luego debe
# eliminar los números terminados en 5, 8, 4 ,0 ,por último vuelva a mostrar el vector. y su
# cantidad de elementos. 

#VALORES DE CONTROL
# VALOR_MINIMO_DEL_RANGO = 1990
# VALOR_MAXIMO_DEL_RANGO = 2022
# VALOR_FUERA_DEL_RANGO = 7777
# BORRAR_TERMINADOS_EN = (5,8,4,0)
# NUMERO_DE_POSICIONES_DEL_ARRAY = 100

# # inicializamos nuestro array y le cargamos "NUMERO_DE_POSICIONES_DEL_ARRAY" valores aleatorios dentro del rango.
# vector5 = arr.array("i", [])

# while len(vector5) < NUMERO_DE_POSICIONES_DEL_ARRAY:
#     numero_aleatorio = r.randint(VALOR_MINIMO_DEL_RANGO,VALOR_MAXIMO_DEL_RANGO)
#     vector5.append(numero_aleatorio)

# print(f"\tel vector5 contiene {len(vector5)} elementos.\n\tvector5:\n",*vector5)

# # Si el ultimo digito del valor esta en "BORRAR_TERMINADOS_EN", le ponemos un valor diferencial "VALOR_FUERA_DEL_RANGO".
# for indice_del_valor,valor in enumerate(vector5):
#     utlimo_digito_del_valor = valor % 10
#     if utlimo_digito_del_valor in BORRAR_TERMINADOS_EN:
#         vector5[indice_del_valor] = VALOR_FUERA_DEL_RANGO

# # depuramos el array del "VALOR_FUERA_DEL_RANGO".
# while VALOR_FUERA_DEL_RANGO in vector5:
#     vector5.remove(VALOR_FUERA_DEL_RANGO)

# print(f"\tel vector5 despues de procesar contiene {len(vector5)} elementos.\n\tvector5:\n",*vector5)

###################################### 67)
# Escriba un programa que llene un vector de 200 posiciones con números aleatorios entre 135
# y 762, debe separar los números impares de los pares, por último muestre los 3 vectores, el
# original , los impares y los pares y la cantidad de elementos por vector

# # valores de control
# POSICIONES_DEL_VECTOR_ORIGINAL = 200
# VALOR_MINIMO_DEL_RANGO = 135
# VALOR_MAXIMO_DEL_RANGO = 762

# # inicializando arrays
# vector6 = arr.array("i",[])
# numeros_pares = arr.array("i", [])
# numeros_impares = arr.array("i", [])

# # cargamos "POSICIONES_DEL_VECTOR_ORIGINAL" valores dentro de "vector6"
# while len(vector6) < POSICIONES_DEL_VECTOR_ORIGINAL:
#     numero_aleatorio = r.randint(VALOR_MINIMO_DEL_RANGO,VALOR_MAXIMO_DEL_RANGO)
#     vector6.append(numero_aleatorio)

# # separamos numeros pares y numeros impares
# for valor in vector6:
#     if valor % 2 == 0:
#         numeros_pares.append(valor)
#     else:
#         numeros_impares.append(valor)

# print(f"El vector original tiene {len(vector6)} elementos.\nEl vector de numeros pares tiene {len(numeros_pares)} elementos.\nEl vector de numeros impares tiene {len(numeros_impares)} elementos.")
# print("VECTOR ORIGINAL:\n",*vector6,"\nVECTOR NUMEROS PARES:\n",*numeros_pares,"\nVECTOR NUMEROS IMPARES:\n",*numeros_impares)

###################################### 68)

# Escriba un programa que simule ser un sorteo al azar con 58 participantes.
# Tenemos sus números de DNI, los participantes tienen números de dni entre 43158258 y
# 44200952, no puede haber participantes repetidos, una vez cargados los dni, debe seleccionar
# 3 ganadores al azar, no se pueden repetir los ganadores, muestre el listado de participantes,
# muestre el número de dni de los ganadores 

# valores de control

# PARTICIPANTES_TOTALES = 58
# VALOR_MINIMO_DEL_DNI = 43158258
# VALOR_MAXIMO_DEL_DNI = 44200952
# NUMERO_DE_GANADORES = 3

# # declaramos el array de participantes y agregamos un total de "PARTICIPANTES_TOTALES" de valores
# parcipantes = arr.array("i",[])

# while len(parcipantes) < PARTICIPANTES_TOTALES:
#     dni_aleatorio = r.randint(VALOR_MINIMO_DEL_DNI,VALOR_MAXIMO_DEL_DNI)
#     if dni_aleatorio not in parcipantes:
#         parcipantes.append(dni_aleatorio)

# # definimos una funcion que nos devuelve "NUMERO_DE_GANADORES" elementos aleatorios(sin repetir) de una lista.
# def ganadores_del_sorteo(lista):
#     lista_de_ganadores = arr.array("i", [])
#     while len(lista_de_ganadores) < NUMERO_DE_GANADORES:
#         elegido_ganador = r.choice(lista)
#         if elegido_ganador not in lista_de_ganadores:
#             lista_de_ganadores.append(elegido_ganador)
    
#     return lista_de_ganadores
# print(f"Los participantes fueron:\n",*parcipantes,f"\n\nY los {NUMERO_DE_GANADORES} ganadores son:",*ganadores_del_sorteo(parcipantes))