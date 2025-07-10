import csv
from collections import namedtuple
# nulo = None
# muy_bajo = 0
# bajo = 25
# moderado = 50
# alto = 75
# muy_alto = 100

Alimento = namedtuple('Alimento', 'nombre , hidratos_de_carbono , proteina , grasas , fibra , azucares_añadidos')

def parseador_csv(direccion_csv):
    with open(direccion_csv, encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  # Saltar la cabecera
        linea = []
        for nombre, hidratos_de_carbono, proteina, grasas, fibra, azucares_añadidos in lector_csv:
            nombre = nombre.strip()
            hidratos_de_carbono = hidratos_de_carbono.strip()
            proteina = proteina.strip()
            grasas = grasas.strip()
            fibra = fibra.strip()
            azucares_añadidos = azucares_añadidos.strip()
            
            linea.append(Alimento(nombre, hidratos_de_carbono, proteina, grasas, fibra, azucares_añadidos))

    return linea
