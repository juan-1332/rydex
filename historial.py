


def consultar_historial():
    print("No hay historial registrado por el momento.")
import json
import os
datos_citas = "datos"
from citas import citas


def consultar_historial():
    print("----- Historial de Citas -----")
    with open(os.path.join(datos_citas, "citas.json"), "r") as archivo:
            citas = json.load(archivo)
    if not citas:
        print("No hay historial registrado por el momento.")
        return

    hay_historial = False
    for cita in citas:
        if "asistio" in cita:
            hay_historial = True

            if cita["asistio"]:
                estado = "Asistio"
            else:
                estado = "No asistio"

            print(
                "Cliente: " + cita["cliente"]
                + " - Fecha: " + cita["fecha"]
                + " - Hora: " + cita["hora"]
                + " - Vehiculo: " + cita["placa"]
                + " - Instructor: " + cita["instructor"]
                + " - Estado: " + estado
                + " - Observaciones: " + cita.get("observaciones", "")
            )

    if not hay_historial:
        print("No hay asistencias registradas por el momento.")

