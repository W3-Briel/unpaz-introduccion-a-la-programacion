NUMERO_ENTERO = int("8")

secreto = bin(NUMERO_ENTERO)[2:]
clave = input("Dime la clave: ")

intentos = 0
while (clave != secreto) & (intentos < 4):
    print("Clave incorrecta")


    
    print(f"este es el intento {intentos+1}")
    intentos+= 1

    if intentos == 3:
        print("te bloqueo la tarjeta bro, disculpa")
        break

    otro_intento = input("quieres introducir otra clave (S/N)?: ")
    if otro_intento.upper() == "S":
        clave = input("Dime la clave: ")
    else:
        break
    


if clave == secreto:
    print("si")


print("*"*10,"\nPrograma terminado\n","*"*10)