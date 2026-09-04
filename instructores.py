import json
import os

instructores = []
datos_instructores = "datos"

def instructor_ya_registrado(nombre):
    nombre_normalizado = nombre.strip().lower()
    for instructor in instructores:
        if instructor["nombre"].lower() == nombre_normalizado:
            return True
    return False


def registrar_instructor():
    while True:
        nombre = input("Ingrese el nombre del instructor: ").strip()
        if not nombre:
            print("Debe ingresar un nombre, no dejar en blanco")
            continue
        if not nombre.replace(" ", "").isalpha():
            print("El nombre no puede ser un numero.")
            continue
        if instructor_ya_registrado(nombre):
            print("Ese instructor ya existe en el sistema. Ingrese otro nombre.")
            continue
        while True:
            tipo_vehiculo = input("Ingrese el tipo de vehiculo que el instructor puede enseñar (moto, carro o ambos): ").strip().lower()
            if tipo_vehiculo not in {"moto", "carro", "ambos"}:
                print("Tipo de vehiculo no valido. Use: moto, carro o ambos.")
                continue
            break

        instructores.append({"nombre": nombre, "tipo_vehiculo": tipo_vehiculo})
        ruta_archivo = os.path.join(datos_instructores, "instructores.json")
        with open(ruta_archivo, "w") as archivo:
            json.dump(instructores, archivo, indent=4)  
        print("Instructor registrado: " + nombre)
        break


def consultar_instructores():
    try:
        with open(os.path.join(datos_instructores, "instructores.json"), "r") as archivo:
            datos = json.load(archivo)
            
            if not datos:
                print("El archivo está vacío, no hay instructores registrados.")
            else:
                print("instructorees registrados:")
                for instructor in datos:
                    print("- " + instructor['nombre'] + "- vehiculo: " + instructor['tipo_vehiculo'])
    except FileNotFoundError:
        print("El archivo no existe, no hay instructores registrados.")


