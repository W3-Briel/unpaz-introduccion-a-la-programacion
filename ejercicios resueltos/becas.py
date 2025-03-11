#condiciones
#distancia >= 40 kilometros
#hermanos > 2
#salario bruto <= 20000

print("programa de becas año 2017")

distacia_escuela = int(input("introduce la distancia a la escuela en kilometros: "))
numero_hermanos = int(input("introduce el numero de hermanos: "))
salario_bruto = int(input("introduce el salario en bruto: "))

print(f"Usted ingreso como dato:\ndistancia: {distacia_escuela}km, hermanos: {numero_hermanos}, salario: ${salario_bruto}")

if (distacia_escuela >= 40) & (numero_hermanos > 2) | (salario_bruto <= 20000):
    print("*" * 10)
    print("se te otorgo la beca")
    print("*" * 10)
else:
    print("X" * 10)
    print("no se te otorgara la beca")
    print("X" * 10)