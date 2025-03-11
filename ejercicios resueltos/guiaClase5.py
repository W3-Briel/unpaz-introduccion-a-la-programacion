############################## 19)
# numero = 0
# while numero < 50:
#     if numero == 0:
#         print(numero)
#         numero += 5
#         print(numero)
#     else:
#         numero += 5
#         print(numero)
############################## 20)
# numero = 2000
# while numero > 0:
#     if numero == 2000:
#         print(numero)
#         numero -= 250
#         print(numero)
#     else:
#         numero-= 250
#         print(numero)
############################## 21)
# palabra = input("ingrese una palabra: ")
# for i in range(10):
#     if i == 0:
#         print(1, palabra)
#     else:
#         print(i+1, palabra)
############################## 22)
def añosCumplidos():
    YEAR = 2023
    edadActual = int(input("cuantos años tienes?: "))

    añoDeNacimiento = YEAR - edadActual
    
    añoLoop = añoDeNacimiento
    contadorDeAños = 0
    while añoLoop <= YEAR:
        if añoLoop == YEAR:
            print(f"en este año {añoLoop} tienes, {contadorDeAños} años de edad.")
            break
        else:
            print(f"en el año {añoLoop} tuviste, {contadorDeAños} años de edad.")
            añoLoop += 1
            contadorDeAños += 1

añosCumplidos()