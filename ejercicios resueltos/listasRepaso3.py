# definimos una funcion que nos cree una lista del largo solicitado por input y pida ingresar sus valores
def creamos_lista():
    LARGO_DE_LA_LISTA = int(input("cuantos elementos tendra tu lista?: "))

    if LARGO_DE_LA_LISTA < 1:
        print("imposible, ERROR")
    else:
        lista_cargada = []

        for indice in range(LARGO_DE_LA_LISTA):
            palabra_a_agregar = input(f"palabra Nº{indice+1} que deseas agregar: ")
            lista_cargada.append(palabra_a_agregar)
            # lista += [palabra]

        print(lista_cargada)

    return lista_cargada

# busca la dada en una lista. y devuelve un texto compuesto con las veces encontradas
def buscar_palabra_en_la_lista(lista):
    palabra_a_buscar = input("que palabra quieres buscar?: ")
    veces_encontrada = list(lista).count(palabra_a_buscar)

    if veces_encontrada < 1:
        print("no se encontraron palabras similares, en la lista.")
    else:
        print(f"la palabra `{palabra_a_buscar}` se encontro {veces_encontrada} veces")

# definimos una funcion para remplazar palabras en una lista
def remplazar_palabra_de_la_lista(lista):
    palabra_a_remplazar = input("que palabra deseas remplazar?: ")

    if palabra_a_remplazar not in lista:
          print("la palabra no se encuentra en la lista")
    else:
        remplazar_por = input("por cual quieres remplazar?: ")

        for indice in range(len(lista)):
            if lista[indice] == palabra_a_remplazar:
                lista[indice] = remplazar_por

        print(lista)

    return lista

# borramos la diferencia(nuestra palabra o palabras), de la lista pasada como parametro.
def eliminar_palabra_de_la_lista(lista):
    palabra_a_eliminar = input("Que palabra quieres eliminar de la lista?: ")

    if palabra_a_eliminar in lista:
        lista_depurada = list(lista)

        while (palabra_a_eliminar in lista_depurada):
            lista_depurada.remove(palabra_a_eliminar)

        print(lista_depurada)
        return lista_depurada
    else:
        print("no se encontro la palabra a eliminar")

# estructura de control
def main():
        LISTA_CARGADA = creamos_lista()
        buscar_palabra_en_la_lista(LISTA_CARGADA)
        LISTA_CON_PALABRA_REMPLAZADA = remplazar_palabra_de_la_lista(LISTA_CARGADA)
        LISTA_DEPURADA = eliminar_palabra_de_la_lista(LISTA_CON_PALABRA_REMPLAZADA)

#llamamos las funcion principal
main()