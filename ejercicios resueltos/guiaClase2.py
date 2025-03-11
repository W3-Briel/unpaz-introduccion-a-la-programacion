# print("hola mundo") # 1)


################################ 2)

# def mostrarNumeros(numeros):
#     inicia=0
#     for i in range(numeros):
#         inicia+=1
#         print(inicia)

# mostrarNumeros(5)

################################ 3)
# for i in range(3):
#     letra= "a"
#     print(letra)
################################ 4)

# def triangulo(letra,base):
#     acumulandoLetras = str(letra)

#     # for i in range(base):
#     #     if i > 0:
#     #         acumulandoLetras += letra
#     #         print(letra + acumulandoLetras)
#     #     else:
#     #         print(letra)
    
#     for i in range(base+1):
#         print(acumulandoLetras*i)



# triangulo("t",5)

################################ 5) - 6)

# nombre = "Angel"
# apellido = "Saucedo"

# print(nombre +" "+ apellido)

# #Angel
# #Saucedo

################################ 7)

# # este programa crea dos variable de tipo number
# numero1 = 15
# numero2 = 20
# # realiza una suma entre ambas variables
# # y a esa suma la divide entre 2
# # por ultimo, al resultado la imprime en pantalla
# print((numero1 + numero2)/2)

############################## 8)

# variable1 = variable2 = variable3 = int(10) #opcion 1

# variable1, variable2, variable3 = 10, 10, 10 #opcion 2

# print(variable1,variable2,variable3)

############################## 9)

# cadena = str("hola mundo")

# print(cadena)

############################## 10)

#variableInvalida1 = mono # error, intentamos asignar un valor de variable que no existen
#variableInvalida2 = "mono" + 2 # error, no podemos realizar operaciones aritmeticas con datos de diferente tipo
#3variableInvalida = "mono" # no se pueden declarar variables con un decimal al principio
#variableInvalida4 = def nombre (): print("hola") # error syntax, no podemos definir de esta manera una funcion

############################## 11)

# variable1, variable2 = "hola", "mundo"
# variable3, variable4 = 123, 321
# variable5, variable6 = 12.3, 32.1
# variable7, variable8 = True, False

# print ("string str():",variable1,",",variable2)
# print ("number int():",variable3,",",variable4)
# print ("float float():",variable5,",",variable6)
# print ("boolean bool():",variable7,",",variable8)

############################## 12)

# OXIGENO = 15.999
# CARBONO = 12.011
# BORO = 10.811

# print("Oxigeno: "+ str(OXIGENO),",","Carbono: " + str(CARBONO),",","Boro: " + str(BORO))

############################## 13) capaz(?)

# variable1, variable2 = "hola", "mundo"
# variable3, variable4 = 123, 321
# variable5, variable6 = 12.3, 32.1
# variable7, variable8 = True, False

# print(type(variable1))
# print(type(variable2))
# print(type(variable3))
# print(type(variable4))
# print(type(variable5))
# print(type(variable6))
# print(type(variable7))
# print(type(variable8))

############################## 14) 

# numero1 = 10
# numero2 = 20

# print (numero1 + numero2)

############################## 15)

# print( ((3+2)/(2*5) )**2 )

############################## 16)

# print( (15/100)*5400)

############################## 17)

# def actividad17():
#     division = 27//5
#     resto = 27%5
#     return print("resto ",resto, "division ",division)

# actividad17()

############################## 18)

# print("el area del triangulo es: ",(20.5 * (20.5)**2)/2)

############################## 19)

# print("el ultimo digito de 58742**2 es: ", (58742**2) % 10)

############################## 20)

# variable1 = int(10)
# variable2 = float(10.5)
# variable3 = True + False
# # se realiza la operacion normalmente, ya que los valores
# # boleanos representan 1 True y, 0 False

# print(variable1 + variable2 + variable3)

############################## 21)

# def pagoCorrespondiente():
#     horas = int(input("horas trabajadas: "))
#     costo = int(input("costo por hora: "))
#     return print(f"por hora ganas ${costo} y trabajaste {horas}hrs, deberias estar recibendo ${horas*costo}")

# pagoCorrespondiente()

############################## 22)

# variable1 = "string"
# variable2 = 0.2
# variable3 = 2
# variable4 = True

# print(variable1, variable2, variable3, variable4)

############################## 23)

# def actividad23(x):
#     return print((x*(x+1))/2)

# actividad23(4)

############################## 25)

# def inversion(cantidadAinvertir,interesAnual,años):
#     porcentaje = cantidadAinvertir * interesAnual / 100
#     return print(f"al final de los {años} años, obtendras\n ${porcentaje} de ganancia")

# inversion(10000,10,1)

############################## 26)

# def logistica(payasos, muñecas):
#     pesoGPayaso = int(112)
#     pesoGMuñeca = int(75)
#     pesoTotal = (pesoGPayaso*payasos)+(pesoGMuñeca*muñecas)
#     prefix = "g"

#     if (pesoTotal > 1000):
#         pesoTotal = pesoTotal / 1000
#         prefix = "Klg"

#     return print(f"En el ultimo pedido, se pidieron: {int(payasos)}, y {int(muñecas)}. \n El peso total del pedido es de {pesoTotal} {prefix}")

# logistica(200, 10)

############################## 27)

# def panaderia(baguettes):
#     precioHabitual = int(50)
#     precioDescuento = (precioHabitual * 60)/100

#     return print(f"Por cada baguette habitualmente son ${precioHabitual}, si compraras {int(baguettes)} pagarias ${baguettes * precioHabitual}.\n Pero comprando con la oferta de las baguettes que no son del dia ahorras 60%, ${precioDescuento} C/U.\nSi compraras {int(baguettes)} pagarias con descuento ${precioDescuento * baguettes}")


# panaderia(100)