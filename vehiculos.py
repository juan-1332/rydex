vehiculos = []


def placa_ya_registrada(placa):
    placa = placa.strip().upper()

    for vehiculo in vehiculos:
        if vehiculo["placa"] == placa:
            return True

    return False


def registrar_vehiculo():
    print("----- Registrar Vehiculo -----")

    while True:
        placa = input("Ingrese la placa del vehiculo: ").strip().upper()

        if placa == "":
            print("La placa no puede estar vacia.")
            continue

        if placa_ya_registrada(placa):
            print("Este vehiculo ya se encuentra registrado.")
            continue

        break

    while True:
        tipo = input(
            "Ingrese el tipo de vehiculo (moto/carro): "
        ).strip().lower()

        if tipo == "moto" or tipo == "carro":
            break

        print("Tipo de vehiculo no valido. Use moto o carro.")

    vehiculos.append({
        "placa": placa,
        "tipo": tipo
    })

    print("Vehiculo registrado correctamente.")
