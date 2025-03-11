#escribir en pantalla de 10 al 1
# for var in range(0,17, 2):
#     print(var," ",end="")

cont = 0
while cont<10:
    cont +=1
    if cont % 2 != 0:
        continue
    print(cont)
    print("hola")