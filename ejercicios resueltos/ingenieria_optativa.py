print("MATERIAS DE INGENIERIA")

listado_materias = ("informatica grafica","pruebas de software","usabilidad y accesibilidad")
print(f"este es el listado de materias {listado_materias}")

optativa = input("que materias deaseas cursar?: ").lower()

if optativa in listado_materias:
    print(f"la materia elegida fue: {optativa} ")
else:
    print("esa asignatura no esta contemplada")