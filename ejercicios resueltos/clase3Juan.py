efectivo = float(input("cuanto fue lo recaudado en efectivo?: "))
credito = float(input("cuanto fue lo recaudado en credito?: "))
mp = float(input("cuanto fue lo recaudado en mercado pago?: "))

def totalRecaudado(efec,credi,mp):
    return efec + credi + mp

def promedioPorMetodosDePago(recaudadoTotal, totalDeMetodosDePago):
    return recaudadoTotal / totalDeMetodosDePago

def mayorMetodo(efectivo,mp,credito):
    if((efectivo > mp) & (efectivo > credito)):
        convertirTipo = str(efectivo)
        texto = str( "Efectivo con -> $ "+ convertirTipo)
        return texto
    elif((mp > efectivo) & (mp > credito)):
        convertirTipo = str(mp)
        texto = str( "Mercado Pago con -> $ "+ convertirTipo)
        return texto
    elif((credito > efectivo) & (credito > mp)):
        convertirTipo = str(credito)
        texto = str( "Credito con -> $ "+ convertirTipo)
        return texto

def menorMetodo(efectivo,mp,credito):
    if((efectivo < mp) & (efectivo < credito)):
        convertirTipo = str(efectivo)
        texto = str( "Efectivo con -> $ "+ convertirTipo)
        return texto
    elif((mp < efectivo) & (mp < credito)):
        convertirTipo = str(mp)
        texto = str( "Mercado Pago con -> $ "+ convertirTipo)
        return texto
    elif((credito < efectivo) & (credito < mp)):
        convertirTipo = str(credito)
        texto = str( "Credito con -> $ "+ convertirTipo)
        return texto

def constructor(efectivo,mp,credito):

    mayor = mayorMetodo(efectivo,mp,credito)
    menor = menorMetodo(efectivo,mp,credito)
    total = totalRecaudado(efectivo,mp,credito)
    promedio = promedioPorMetodosDePago(total, 3)

    return print(f"El monto total fue de ${total} con, un promedio de ${promedio} por metodo de pago. \nEl metodo de pago con mayor recaudacion fue {mayor}, y el que obtuvo menor recaudacion fue {menor}.")

constructor(efectivo,mp,credito)