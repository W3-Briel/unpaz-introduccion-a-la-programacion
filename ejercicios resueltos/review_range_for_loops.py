#  range(a,b,c)
# import time
# flush = true
# valor:02d
# for i in palabra: que hace i

# listas
# renombrar un objeto de la lista
# end=""
# break en for
# else en for
# investigar mas format en python

##############################################

variable = ["elemento1","elemento2","elemento3"]
variable2 = "hola"

#crea una lista de tuplas con un valor int incremental, tiene que ser un objeto iterable.

    # print(list(enumerate(variable)))
    # print(list(enumerate(variable2)))

#podemos decirle desde que numero vamos a empezar a enumerar
    # print(list(enumerate(variable,5)))
    # print(list(enumerate(variable2,5)))

# creamos un for//loop// con una varible//var// que itera en el rango//range(...)// del largo//len(variable2)// del string//variable2//,
# luego utilizando un print, enumeramos cada caracter o elemento y lo convertimos en una lista //list(enumerate(variable2))
# y ya que enumerate(), crea una lista de tuplas, debemos entrar primero al index, utilizando el valor int del for. //list(enumerate(variable2))[var]
# y por ultimo entramos al elemento de la tupla, ya que en el index 0 estara el numero, y en el 1 estara el elemento. //list(enumerate(variable2))[var][1]

    # for var in range(len(variable2)):
    #     print(list(enumerate(variable2,1))[var][0],
    #           list(enumerate(variable2))[var][1])

# refactorizando el codigo anterior
    # for var in range(len(variable2)):
    #     elemento_caracter_enumerado = list(enumerate(variable2,1))[var]
    #     print(elemento_caracter_enumerado[0],elemento_caracter_enumerado[1])

##############################################

# utilizando la funcion range(inicio, final, saltos)
# se puede crear una lista de numeros// list(range(...))

# variable3 = list(range(0,5))
    # print(variable3) # [0, 1, 2, 3, 4]

# como toda lista, se puede iterar.
    # for i in variable3:
    #     print(variable3[i])

# rango, arranca en 1, el tope es 10, y va de a 2 en 2.
    # for i in range(1,10,2):
    #     print(i)

# utilizamos el largo de una variable como rango //range(..)//
    # for i in range(len(variable2)):
    #     print(i)

##############################################

# detalles del for loop

# la variable "i" tomara el valor de cada posicion de la variable2.
    # for i in variable2:
    #     print(i)

