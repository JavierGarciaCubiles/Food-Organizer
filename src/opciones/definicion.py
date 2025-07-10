# Hidratos de Carbono Bajos o Muy Bajos, 
# Proteínas Altas o Muy Altas, 
# Grasas Muy Bajas o Bajas ,
# Fibra Moderada, Alta o Muy Alta,
# Azúcares Añadidos deben ser Nulos o Muy Bajos.

import parseador
import random

lineas_desayuno = parseador.parseador_csv("data/Breakfast-Database")
lineas_almuerzo = parseador.parseador_csv("data/Dinner-Database")
lineas_cena = parseador.parseador_csv("data/Breakfast-Database")

def filtrar_definicion(lineas_desayuno):
    res = []
    for linea in lineas_almuerzo:
        if linea.hidratos_de_carbono in ["Muy Bajo", "Bajo"] and \
           linea.proteina in ["Alto", "Muy Alto"] and \
           linea.grasas in ["Muy Bajo", "Bajo"] and \
           linea.fibra in ["Moderado", "Alto", "Muy Alto"] and \
           linea.azucares_añadidos in ["Muy Bajo"] or linea.azucares_añadidos is None or linea.azucares_añadidos in ["Bajo"]:
            res.append(linea)
    return res

def obtener_opcion_definicion():
    desayuno = random.choice(filtrar_definicion(lineas_desayuno))
    almuerzo = random.choice(filtrar_definicion(lineas_almuerzo))
    cena = random.choice(filtrar_definicion(lineas_cena))

    return {
        "desayuno": desayuno,
        "almuerzo": almuerzo,
        "cena": cena
    }