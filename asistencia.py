import json
import os

from citas import citas
from clientes import clientes
datos_citas = "datos"

def buscar_cliente(documento_cliente):
    try:
        with open(os.path.join(datos_citas, "clientes.json"), "r") as archivo:
            clientes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se pudo cargar el archivo de clientes.")
        return None

    for cliente in clientes:
        if cliente["documento"] == documento_cliente:
            return cliente
    return None


def obtener_citas_cliente(documento_cliente):
    citas_cliente = []
    with open(os.path.join(datos_citas, "citas.json"), "r") as archivo:
        datos = json.load(archivo)
    citas.clear()
    citas.extend(datos)
    for cita in citas:
        if cita["documento"] == documento_cliente:
            citas_cliente.append(cita)
    return citas_cliente


def mostrar_cita(indice, cita):
    print(
        str(indice)
        + ". "
        + cita["fecha"]
        + " "
        + cita["hora"]
        + " - Vehiculo: "
        + cita["placa"]
        + " - Instructor: "
        + cita["instructor"]
    )


def seleccionar_cita(citas_cliente):
    while True:
        opcion = input("Seleccione el numero de la cita: ").strip()
        try:
            indice = int(opcion)
        except ValueError:
            print("Entrada invalida. Seleccione un numero.")
            continue

        if 1 <= indice <= len(citas_cliente):
            return citas_cliente[indice - 1]

        print("Opcion de cita invalida.")


def registrar_asistencia(cita):
    observaciones_cita(cita)
    while True:
        respuesta = input("¿El cliente asistio a la cita? (si/no): ").strip().lower()
        if respuesta == "si":
            cita["asistio"] = True
            print("Asistencia registrada correctamente.")
            break
        if respuesta == "no":
            cita["asistio"] = False
            print("Inasistencia registrada correctamente.")
            break
        print("Respuesta invalida. Use 'si' para si o 'no' para no.")

    if "observaciones" not in cita:
        cita["observaciones"] = ""

    with open(os.path.join(datos_citas, "citas.json"), "w") as archivo:
        json.dump(citas, archivo, indent=4)


def observaciones_cita(citas):
    while True:
        opcion = input(
            "¿Desea agregar observaciones a la cita? (si/no): "
        ).strip().lower()
        if opcion == "si":
            observacion = input("Ingrese la observacion: ").strip()
            citas["observaciones"] = observacion
            print("Observacion registrada correctamente.")
            return 
        if opcion == "no":
            print("No se agregaron observaciones.")
            return
        print("Respuesta invalida. Use 'si' para si o 'no' para no.")   
def controlar_asistencia():
    print("----- Controlar Asistencia -----")
    try:
        with open(os.path.join(datos_citas, "clientes.json",), "r") as archivo:
            clientes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se pudo cargar el archivo de clientes.")
        return
    
    if not clientes:
        print("No hay clientes registrados.")
        return

    documento_cliente = input("Ingrese el documento del cliente: ").strip()
    if not documento_cliente:
        print("El documento del cliente no puede estar vacio.")
        return

    cliente = buscar_cliente(documento_cliente)
    if cliente is None:
        print("Cliente no encontrado.")
        return

    citas_cliente = obtener_citas_cliente(cliente["documento"])
    if not citas_cliente:
        print("El cliente no tiene citas.")
        return

    print("Citas de " + cliente["nombre"] + ":")
    for indice, cita in enumerate(citas_cliente, start=1):
        mostrar_cita(indice, cita)

    cita_seleccionada = seleccionar_cita(citas_cliente)
    registrar_asistencia(cita_seleccionada)