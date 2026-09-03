import re
from datetime import datetime, timedelta


citas = []


def fecha_y_hora_validas(fecha, hora):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fecha):
        return None

    if not re.fullmatch(r"\d{2}:\d{2}", hora):
        return None

    try:
        return datetime.strptime(fecha + " " + hora, "%Y-%m-%d %H:%M")
    except ValueError:
        return None

def cita_se_cruza(fecha_hora, cita):
    fecha_hora_cita = fecha_y_hora_validas(cita["fecha"], cita["hora"])
    if fecha_hora_cita is None:
        return False

    fin_nueva_cita = fecha_hora + timedelta(hours=1)
    fin_cita_existente = fecha_hora_cita + timedelta(hours=1)
    return fecha_hora < fin_cita_existente and fecha_hora_cita < fin_nueva_cita


def vehiculo_ocupado(placa, fecha_hora):
    for cita in citas:
        if cita["placa"] == placa and cita_se_cruza(fecha_hora, cita):
            return True
    return False


def instructor_ocupado(nombre, fecha_hora):
    for cita in citas:
        if cita["instructor"].lower() == nombre.lower() and cita_se_cruza(fecha_hora, cita):
            return True
    return False


def programar_cita():
    from clientes import clientes
    from instructores import instructores
    from vehiculos import vehiculos

    print("----- Programar Cita -----")
    nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
    cliente_encontrado = None

    for cliente in clientes:
        if cliente["nombre"].lower() == nombre_cliente.lower():
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("Cliente no encontrado. Por favor, registre al cliente primero.")
        return

    print("Cliente encontrado: " + cliente_encontrado["nombre"])

    vehiculos_cliente = []
    for vehiculo in vehiculos:
        tipo_cliente = cliente_encontrado["tipo_vehiculo"]
        puede_usar_vehiculo = tipo_cliente == "ambos" or vehiculo["tipo"] == tipo_cliente
        if puede_usar_vehiculo:
            vehiculos_cliente.append(vehiculo)

    if not vehiculos_cliente:
        print("No hay vehiculos compatibles con el cliente.")
        return

    while True:
        fecha_cita = input("Ingrese la fecha de la cita (YYYY-MM-DD): ").strip()
        hora_cita = input("Ingrese la hora de la cita (HH:MM): ").strip()
        fecha_hora = fecha_y_hora_validas(fecha_cita, hora_cita)
        if fecha_hora is None:
            print("Fecha u hora no valida. Use YYYY-MM-DD y HH:MM.")
            continue
        break

    vehiculos_disponibles = []
    for vehiculo in vehiculos_cliente:
        if not vehiculo_ocupado(vehiculo["placa"].upper(), fecha_hora):
            vehiculos_disponibles.append(vehiculo)

    if not vehiculos_disponibles:
        print("No hay vehiculos disponibles para esa fecha y hora.")
        return

    print("Vehiculos disponibles:")
    for indice, vehiculo in enumerate(vehiculos_disponibles, start=1):
        print(str(indice) + ". Placa: " + vehiculo["placa"] + " - Tipo: " + vehiculo["tipo"])

    while True:
        opcion_vehiculo = input("Seleccione el numero del vehiculo: ").strip()
        try:
            indice_vehiculo = int(opcion_vehiculo)
        except ValueError:
            print("Entrada invalida. Seleccione un numero.")
            continue
        if 1 <= indice_vehiculo <= len(vehiculos_disponibles):
            vehiculo_seleccionado = vehiculos_disponibles[indice_vehiculo - 1]
            break
        print("Opcion de vehiculo invalida.")

    instructores_disponibles = []
    for instructor in instructores:
        tipo_instructor = instructor["tipo_vehiculo"]
        puede_dar_clase = tipo_instructor == "ambos" or tipo_instructor == vehiculo_seleccionado["tipo"]
        if puede_dar_clase and not instructor_ocupado(instructor["nombre"], fecha_hora):
            instructores_disponibles.append(instructor)

    if not instructores_disponibles:
        print("No hay instructores disponibles para esa fecha y hora.")
        return

    print("Instructores disponibles:")
    for indice, instructor in enumerate(instructores_disponibles, start=1):
        print(str(indice) + ". " + instructor["nombre"])

    while True:
        opcion_instructor = input("Seleccione el numero del instructor: ").strip()
        try:
            indice_instructor = int(opcion_instructor)
        except ValueError:
            print("Entrada invalida. Seleccione un numero.")
            continue
        if 1 <= indice_instructor <= len(instructores_disponibles):
            instructor_seleccionado = instructores_disponibles[indice_instructor - 1]
            break
        print("Opcion de instructor invalida.")

    nueva_cita = {
        "cliente": cliente_encontrado["nombre"],
        "placa": vehiculo_seleccionado["placa"].upper(),
        "instructor": instructor_seleccionado["nombre"],
        "fecha": fecha_cita,
        "hora": hora_cita,
        "duracion_horas": 1,
    }
    citas.append(nueva_cita)

    print("Cita programada para " + nueva_cita["cliente"] + ".")
    print("Vehiculo: " + nueva_cita["placa"])
    print("Instructor: " + nueva_cita["instructor"])
    print("Fecha y hora: " + nueva_cita["fecha"] + " " + nueva_cita["hora"])
    return nueva_cita

