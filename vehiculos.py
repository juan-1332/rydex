vehiculos = []


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

        while True:
            tipo = input("Ingrese el tipo de vehiculo (moto/carro): ").strip().lower()
            if tipo in {"moto", "carro"}:
                placa = placa.upper()
                vehiculos.append({"placa": placa, "tipo": tipo})
                print("Vehiculo registrado: " + placa)
                return

            print("Tipo de vehiculo no valido. Use moto o carro.")
        

def consultar_vehiculos():
    if not vehiculos:
        print("No hay vehiculos registrados.")
        return

    print("Vehiculos registrados:")
    for i, vehiculo in enumerate(vehiculos, start=1):
        print(str(i) + ". " + vehiculo['tipo'] + " - " + vehiculo['placa'])
