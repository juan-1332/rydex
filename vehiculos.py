import json
import os

vehiculos = []
datos_vehiculos = "datos"

def placa_ya_registrada(placa):
    placa = placa.strip().upper()
    for vehiculo in vehiculos:
        if vehiculo["placa"].upper() == placa:
            return True
    return False


def registrar_vehiculo():
    while True:
        placa = input("Ingrese la placa del vehiculo: ").strip()
        if not placa:
            print("La placa no puede estar vacia.")
            continue

        if placa_ya_registrada(placa):
            print("Esta placa ya esta registrada. Ingrese otra placa.")
            continue

        break

    while True:
        tipo = input("Ingrese el tipo de vehiculo (moto/carro): ").strip().lower()
        if tipo in {"moto", "carro"}:
            placa = placa.upper()
            vehiculos.append({"placa": placa, "tipo": tipo})
            ruta_archivo = os.path.join(datos_vehiculos, "vehiculos.json")
            with open(ruta_archivo, "w") as archivo:
                     json.dump(vehiculos, archivo, indent=4)    
            print("Vehiculo registrado con placas: " + placa)
            return
        print("Tipo de vehiculo no valido. Use moto o carro.")
         
    

def consultar_vehiculos():
    try:
        with open(os.path.join(datos_vehiculos, "vehiculos.json"), "r") as archivo:
            datos = json.load(archivo)
            
            if not datos:
                print("El archivo está vacío, no hay vehículos registrados.")
            else:
                print("vehiculos registrados:")
                for vehiculo in datos:
                    print("- " + "Placa: " + vehiculo['placa'] + " - Tipo: " + vehiculo['tipo'])
    except FileNotFoundError:
        print("El archivo no existe, no hay vehículos registrados.")




