#titulo
print("programa que suma, resta y potencia dos numeros")

#declaracion de funciones
def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def potenciacion(x,y):
    return x**y

def mayor_menor(x,y):
    if x>y:
        print("el numero mayor: ",x)
    elif x<y:
        print("el nunmero mayor: ",y)
    else:
        print("ambos numeros son iguales ",x," ",y)

def mensaje():
    print("fin del programa")

#proceso

# for i in range(3):
#     print('*' *80)

#     x=int(input("ingrese el primer numero: "))
#     y=int(input("ingrese el segundo numero: "))

#     #llamamos a las funciones correspondientes

#     print("la suma de ambos numeros es: ",suma(x,y))

#     print("la resta de ambos numeros es: ", resta(x,y))

#     print("la potenciacion de ambos numeros es: ",potenciacion(x,y))

#     mayor_menor(x,y)

count = 0

while count < 3:
    print('*' *80)

    x=int(input("ingrese el primer numero: "))
    y=int(input("ingrese el segundo numero: "))

    #llamamos a las funciones correspondientes

    print("la suma de ambos numeros es: " + str(suma(x,y)))

    print("la resta de ambos numeros es: "+ str(resta(x,y)))

    print("la potenciacion de ambos numeros es: "+ str(potenciacion(x,y)))

    mayor_menor(x,y)

    count += 1

# mensaje de fin del programa
mensaje()