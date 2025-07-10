# Hidratos de Carbono Moderados o Altos, 
# Proteínas Moderadas o Altas, 
# Grasas Bajas o Moderadas , 
# Fibra Moderada, Alta o Muy Alta,
# Azúcares Añadidos deben ser Nulos o Muy Bajos.

import parseador
import random

lineas_desayuno = parseador.parseador_csv("data/Breakfast-Database")
lineas_almuerzo = parseador.parseador_csv("data/Dinner-Database")
lineas_cena = parseador.parseador_csv("data/Breakfast-Database")

def filtrar_mantenimiento(lineas_desayuno):
    res = []
    for linea in lineas_almuerzo:
        if linea.hidratos_de_carbono in ["Moderdo", "Alto"] and \
           linea.proteina in ["Moderdo", "Alto"] and \
           linea.grasas in ["Bajo", "Moderado"] and \
           linea.fibra in ["Moderado", "Alto", "Muy Alto"] and \
           linea.azucares_añadidos in ["Muy Bajo"] or linea.azucares_añadidos is None or linea.azucares_añadidos in ["Bajo"]:
            res.append(linea)
    return res



def obtener_opcion_mantenimiento():
    desayuno = random.choice(filtrar_mantenimiento(lineas_desayuno))
    almuerzo = random.choice(filtrar_mantenimiento(lineas_almuerzo))
    cena = random.choice(filtrar_mantenimiento(lineas_cena))

    return {
        "desayuno": desayuno,
        "almuerzo": almuerzo,
        "cena": cena
    }