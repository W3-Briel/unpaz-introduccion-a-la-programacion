############################## 10)

# def cuantosAñosPasaron(añoCrudo):
#     año = int(añoCrudo)
#     añoActual = 2023
#     diferenciaDeAños = añoActual - año
#     haceCuanto = " "
#     edad = "menor"

#     if diferenciaDeAños >= 18:
#         edad = "mayor"
#         auxiliar  = diferenciaDeAños - 18
#         haceCuanto = str("usted es mayor hace ")
#         haceCuanto += str(auxiliar) + " años"
    

#     return print(f"Han pasado {diferenciaDeAños} años. Por lo tanto usted es {edad} de edad. {haceCuanto}")

# cuantosAñosPasaron(input("ingresa: "))

############################## 11)

# def bolean():
#     boleanoNumber = int(input("ingresa un numero 0 o 1: "))

#     if (boleanoNumber < 0) | (boleanoNumber > 1):
#         return print("deberia ser 0 o 1")
#     else:
#         return print( bool(boleanoNumber) )

# bolean()

############################## 12)

# def vocalOconsonante(letraCrude):
#     letra = str(letraCrude)

#     if len(letra) > 1:
#         return print("solo puedes ingresar una letra.")
#     elif letra.count("a") | letra.count("e") | letra.count("i") | letra.count("o") | letra.count("u"):
#         return print("la letra es vocal ", letra)
#     else:
#         return print("la letra consonante ", letra)



# vocalOconsonante(input("ingresa una letra: "))

############################## 13)

# def vacaciones(mesCrudo):
#     mes = int(mesCrudo)

#     if (mes < 1) | (mes > 12):
#         return print("ingrese un mes del año")
#     elif (mes == 1) | (mes == 2) | (mes == 3) | (mes == 12):
#         return print("Mar del plata \nSanta Teresita \nCordoba \nSan luis")
#     elif (mes == 6) | (mes == 7) | (mes == 8):
#         return print("Cataratas \nBariloche\nPerito Moreno")
#     else:
#         return print("No tenemos suguerencias cargadas")

# vacaciones(input("ingrese un mes: "))

############################## 14)

# def calcular(n1Crudo,n2Crudo,n3Crudo):
#     n1,n2,n3 = int(n1Crudo), int(n2Crudo),int(n3Crudo)
#     suma = n1 + n2 + n3

#     if suma > 50:
#         return print(f"el resultado despues de divir es {suma / 2}, sin dividir es {suma}")
#     elif suma < 50:
#         suma = suma**3
#         if suma > 5000:
#             return print("Este es un gran numero")
#         else:
#             return print("el numero es: ",suma)

# calcular(20,10,10)

############################## 15)

# def comparaNumeros(n1Crudo,n2Crudo):
#     n1, n2 = int(n1Crudo), int(n2Crudo)

#     if n1 > n2:
#         return print(f"{n1} es mayor a {n2}")
#     elif n1 < n2:
#         return print(f"{n1} es menor a {n2}")
#     else:
#         return print(f"{n1} y {n2} son iguales")

# comparaNumeros(input("ingresa el numero 1: "),input("ingresa el numero 2: "))

############################## 16)

# def calculosAritmeticos():
#     operacion = int(input("MENU:\nSuma(1)\nResta(2)\nMultiplicacion(3)\nIngrese el indice de la operacion que deseas realizar: "))
#     n1,n2 = int(input("dato 1: ")), int(input("datos 2: "))

#     match operacion:
#         case 1: 
#             return print(f" {n1} + {n2} = {n1 + n2}")
#         case 2:
#             return print(f" {n1} - {n2} = {n1 - n2}")
#         case 3:
#             return print(f" {n1} * {n2} = {n1 * n2}")
#         case _:
#             return print("opcion incorrecta")

# calculosAritmeticos()

############################## 17)

# def comidas(horaCrudo):
#     hora = str(horaCrudo).split(":")

#     match hora[0]:
#         case "10":
#             return print("es hora del Desayuno")
#         case "13":
#             return print("es hora del Almuerzo")
#         case "17":
#             return print("es hora de la Merienda")
#         case "21":
#             return print("es hora de la Cena")
#         case _:
#             return print("no es hora de comer.")

# comidas(input("ingrese una hora: "))

##############################