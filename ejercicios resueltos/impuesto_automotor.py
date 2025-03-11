#impuesto = año  y tipo(P, T , R)
#diferencia de años, 2023 - año del modelo

# impuesto P, años < 10 $200, años > 10 | años <= 20
# excluir p, si años > 20

#impueto T, (años < 10 $200, años > 10 & años <= 20
# excluir p, si años > 20) + 150 de licencia bro

#impuesto R, año * 100

def impuesto_automotor(años):
    tipo = input("P: particular, T: taxis, R: remis\n INGRESE TIPO DE AUTO: ").upper()
    diferencia_de_años = 2023 - años

    match tipo:
        case "P":
            if diferencia_de_años < 10:
                print("pagas $200 de impuesto automotor")
            elif (10 > diferencia_de_años < 20) | (diferencia_de_años == 20):
                print("pagas $150 de impuesto automotor")
            else:
                print("no pagas impuesto automotor")
        case "T":
            licencia = 150

            if diferencia_de_años < 10:
                print(f"pagas $200 de impuesto automotor mas $150 de licencia.\n en total se pagaria ${200+licencia}")
            elif (10 > diferencia_de_años < 20) | (diferencia_de_años == 20):
                print(f"pagas $150 de impuesto automotor mas $150 de licencia.\n en total se pagaria ${150+licencia}")
            else:
                print("no pagas impuesto automotor, pero debes pagar la licencia, son $150")
        case "R":
                print(f"pagarias ${diferencia_de_años * 100},y en el año 2028 pagarias ${100*(2028-años)}")
            # while diferencia_de_años > 0:
            #     print(f"en el año {año_actual} pagarias ${diferencia_de_años * 100}")

            #     año_actual+= 1
            #     diferencia_de_años -= 1

impuesto_automotor(int(input("ingrese el año del vehiculo: ")))
