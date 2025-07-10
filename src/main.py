from opciones.definicion import obtener_opcion_definicion
from opciones.mantenimiento import obtener_opcion_mantenimiento
from opciones.volumen import obtener_opcion_volumen


if __name__ == "__main__":
    # 3 opciones, Volumen, Definición, Mantenimiento
    opcion = input("¿Qué tipo de dieta quieres? (Volumen, Definición, Mantenimiento): ").strip().lower()
    if opcion == "volumen":
        print(obtener_opcion_volumen())
    elif opcion == "definición":
        print(obtener_opcion_definicion())
    elif opcion == "mantenimiento":
        print(obtener_opcion_mantenimiento())
    

