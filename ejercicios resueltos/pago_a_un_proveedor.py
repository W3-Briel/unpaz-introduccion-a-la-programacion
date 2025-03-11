#A si el monto a pagar > 1000 se aplica dEscuento de 5%
#B si el monto esta entre > 1500 & <2500 se aplica descuento del 2%
#si no se cumple ninguna de las condiciones no se aplica descuento

monto =float (input('ingrese el monto a pagar:'))
if monto > 1000:
    descuento = monto * 0.05
    print(monto - descuento)
else:
    descuento=0