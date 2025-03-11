import random

print("juego de PIERDA, PAPEL o TIJERA, HUMANO VS MAQUINA")


elementos = ("piedra", "papel", "tijera")
maquina  = random.choice(elementos)
humano = input("elige PIEDRA, PAPEL, TIJERA: ").lower()

def ganador(PC, elijo):
    if PC == elijo:
        return print("EMPATE")
    else:
        match elijo:
            case "piedra":
                if str(PC) == "tijera":
                        return print(f"GANASTE - la maquina elige {PC}")
                else:
                    return print(f"PERDISTE, la maquina eligio {PC}")
            case "papel":
                if str(PC) == "piedra":
                    return print(f"GANASTE - la maquina elige {PC}")
                else:
                    return print(f"PERDISTE, la maquina eligio {PC}")
            case "tijera":
                if str(PC) == "papel":
                    return print(f"GANASTE - la maquina elige {PC}")
                else:
                    return print(f"PERDISTE, la maquina eligio {PC}")
            # case _:
            #     return print("la maquina eligio", PC)

ganador(maquina,humano)


# menu para seleccionar
# seleccionar piedra papel o tijeras

# tijera 2 gana a papel 1, pierde con piedra 0 y empata con tijera 2
# papel 1 gana con piedra 0 pierde con tijera 2, gana con piedra y empata con papel 1
# piedra 0 gana con tijera 2, pierde con papel 1 y empata con piedra 0

# if humano == maquina:
#     print("empate")
# elif humano == "piedra":
#         if maquina == "tijera":
#              print("humano gana")
#         else:
#              print ("maquina gana")
# elif humano == "papel":
#         if maquina == "piedra":
#              print("humano gana")
#         else:
#              print ("maquina gana")
# elif humano == "tijera":
#         if maquina == "papel":
#              print("humano gana")
#         else:
#              print ("maquina gana")