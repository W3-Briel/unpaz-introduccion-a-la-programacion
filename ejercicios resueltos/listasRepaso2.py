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

# definimos funcion para buscar y contar una palabra en la lista
def buscar_palabra_en_la_lista(lista):
    palabra_a_buscar = input("que palabra quieres buscar?: ")    
    veces_encontrada = list(lista).count(palabra_a_buscar)
    if veces_encontrada < 1:
        print("no se encontraron palabras similares, en la lista.")
    else:
        print(f"la palabra `{palabra_a_buscar}` se encontro {veces_encontrada} veces")

def main():
        # le establecemos la lista cargada en una constante
        LISTA_CARGADA = creamos_lista()
        #llamamos la funcion de buscar y le pasamos como parametro la lista cargada "LISTA_CARGADA"
        buscar_palabra_en_la_lista(LISTA_CARGADA)

#llamamos las funcion principal
main()