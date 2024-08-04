##
## al programar podemos llegar al mismo resultado de diferentes maneras, por lo general, aunque se pueda hacer de alguna forma
## si en alguna parte de tu codigo lo haces de tal manera, la proxima vez que hagas algo similiar, deberia ser similar el codigo.

## seria como tener una consistencia. si usas fstrings para tu codigo, usalo en todos lados.
## asi con los espacios, si usas 2, usa 2. si usas 4, usa 4. blablabla

## al final esto ayudara a poder leer tu codigo, lo que es muy importante.
## aparte de intentar tener un codigo consistente:

## 2) investigar las convecciones y estandares que se utilizan al escribir el lenguaje
## 3) mas adelante deberias implementar buenas practicas
## 4) y bueno, aun mas adelante, te vas a encontrar con temas como la optimizacion, complejidad algoritmica...

## todo esto te va a llevar a tener un codigo mantenible, facil de leer, y seguro que muchas cosas mas jasdfjasjdf
## el tema es que todo esto se consigue con la experiencia y tiempo de estudio.

## entonces, bueno, como dije, se puede resolver las problematicas de diferentes maneras
## pero no todas las maneras de resolver un problema es la mejor.


entrada_usuario = input("ingresar un valor: ")
print("1(esto es concatenacion de strings)lo que ingreso el usuario es: "+ entrada_usuario)
print(f"2(esto fue hecho con un fstring)lo que ingreso el usuario es: {entrada_usuario}")

##Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
##número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = int(input("cantidad a invertir: "))
interes = int(input("interes anual: "))
años = int(input("cantidad de años: "))

print(f"la cantidad que vas a ganar al terminar el plazo, es: {(inversion * (interes/100)) * años }")

###
