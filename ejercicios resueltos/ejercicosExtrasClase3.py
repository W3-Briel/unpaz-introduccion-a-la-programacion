############################## 1)

# def altura():
#     altura = float(input("Ingresa tu altura en metros: "))
#     alturaMetros = str(altura) + " metros"
#     alturaCentimetros = str(altura*100) + " centimetros"

#     return print(f"usted mide {alturaMetros} o {alturaCentimetros}")

# altura()

############################## 2)

# def caracteresNombre():
#     nombreCompleto = input("Ingrese su nombre completo: ")
#     caracteres = len(nombreCompleto)

#     if (nombreCompleto.count(" ") > 0):
#         caracteres = len(nombreCompleto) - nombreCompleto.count(" ")

#     return print(f"tu nombre completo es {nombreCompleto} y en total, tiene {caracteres} caracteres")

# caracteresNombre()

############################## 3)

# def derechoYrevez():
#     nombreCompleto = input("Ingrese su nombre completo: ")
#     nombres = nombreCompleto.split(" ")
#     primerNombre = str(nombres[0])
#     largo = len(primerNombre)

#     nombreAlrevez = ""

#     loop = largo-1
#     while loop >= 0:
#         nombreAlrevez += primerNombre[loop]
#         loop -= 1


#     return print(f"tu primer nombre es {nombres[0].capitalize()}.\n Al revez se escribe: {nombreAlrevez}")

# derechoYrevez()

############################## 4)

# print("Escribir un programa que corte muestre por pantalla los últimos 40 caracteres de este enunciado."[40:])

############################## 5)

def fecha(ddmmaaaa):
    fecha = str(ddmmaaaa).split("/")
    dia = fecha[0]
    mes = fecha[1]
    año = fecha[2]

    if int(dia) > 31:
        return print("tiene que ser un dia correcto")
    elif int(mes) > 12:
           return print("tiene que ser un mes correcto")
    elif int(año) > 5000:
        return print("problablemete el mundo no exista en ese año")
    else:
        return print(f"ingresaste {ddmmaaaa}.\ndia: {dia}\nmes: {mes}\naño: {año}")

fecha(input("introduce la fecha en formato dd/mm/aaaa: "))

############################## 6)

# def cincoPalabras():
#     palabras = input("Escribe una oracion de 5 palabras o menos: ")
#     contador = palabras.split(" ")

#     if len(contador) > 5:
#         return print("te pasaste de las 5 palabras")
#     else:
#         print(palabras.upper(), "mayusculas")
#         print(palabras.lower(), "minusculas")
#         print(palabras.capitalize(), "capitalize")
    
#     return print("--- fin del programa ---")

# cincoPalabras()

############################## 7)

# def letra():
#     letra = input("envia una letra: ").lower()
#     return print(f"usted envio la letra -> {letra}.")

# letra()

############################## 8)

# def dosDigitos():
#     strNumero = input("ingresa un numero de dos digitos: ")
#     intNumero = int(strNumero)

#     if len(strNumero)>2:
#         return print("maximo dos digitos")
#     elif intNumero < 20:
#         return print(intNumero/2)
#     else:
#         return print(intNumero)

# dosDigitos()

############################## 9)

# def nota(notaCruda):
#     nota = float(notaCruda)

#     if (nota < 0) | (nota > 10):
#         return print("deberias poner una nota real")
#     elif nota < 4:
#         return print("desaprobado")
#     elif 4 >= nota <= 6:
#         return print("aprobado")
#     elif nota > 7:
#         return print("promocionado")

# nota(input("ingresa la nota: "))