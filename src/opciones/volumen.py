# Hidratos de Carbono Altos o Moderados, 
# Proteínas Altas o Muy Altas, 
# Grasas Moderadas o Altas , 
# Fibra Moderada, Alta o Muy Alta,
# Azúcares Añadidos deben ser Nulos o Muy Bajos.

import parseador
import random

lineas_desayuno = parseador.parseador_csv("data/Breakfast-Database")
lineas_almuerzo = parseador.parseador_csv("data/Dinner-Database")
lineas_cena = parseador.parseador_csv("data/Breakfast-Database")

def filtrar_volumen(lineas_desayuno):
    res = []
    for linea in lineas_almuerzo:
        if linea.hidratos_de_carbono in ["Moderado", "Alto"] and \
           linea.proteina in ["Alto", "Muy Alto"] and \
           linea.grasas in ["Moderado", "Alto"] and \
           linea.fibra in ["Moderado", "Alto", "Muy Alto"] and \
           linea.azucares_añadidos in ["Muy Bajo"] or linea.azucares_añadidos is None or linea.azucares_añadidos in ["Bajo"]:
            res.append(linea)
    return res


def obtener_opcion_volumen():
    desayuno = random.choice(filtrar_volumen(lineas_desayuno))
    almuerzo = random.choice(filtrar_volumen(lineas_almuerzo))
    cena = random.choice(filtrar_volumen(lineas_cena))

    return {
        "desayuno": desayuno,
        "almuerzo": almuerzo,
        "cena": cena
    }