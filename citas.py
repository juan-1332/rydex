
citas = []

def programar_cita():
    from clientes import clientes
    from vehiculos import vehiculos
    from citas import citas

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

    print("Vehículos registrados para este cliente:")

    vehiculos_cliente = [
        v for v in vehiculos
        if v["cliente"] == cliente_encontrado["nombre"]
    ]

    if not vehiculos_cliente:
        print("No hay vehículos registrados para este cliente.")
        return

    for idx, vehiculo in enumerate(vehiculos_cliente, start=1):
        print(
            str(idx) + ". Placa: " +
            vehiculo["placa"] +
            ", Modelo: " +
            vehiculo["modelo"]
        )

    opcion_vehiculo = input(
        "Seleccione el número del vehículo para la cita: "
    ).strip()

    try:
        opcion_vehiculo = int(opcion_vehiculo)

        if 1 <= opcion_vehiculo <= len(vehiculos_cliente):

            vehiculo_seleccionado = vehiculos_cliente[opcion_vehiculo - 1]

            fecha_cita = input(
                "Ingrese la fecha de la cita (YYYY-MM-DD): "
            ).strip()

            hora_cita = input(
                "Ingrese la hora de la cita (HH:MM): "
            ).strip()

            cita = {
                "cliente": cliente_encontrado["nombre"],
                "documento": cliente_encontrado["documento"],
                "vehiculo": vehiculo_seleccionado["placa"],
                "fecha": fecha_cita,
                "hora": hora_cita
            }

            citas.append(cita)

            print()
            print("----- Cita programada correctamente -----")
            print("Cliente: " + cliente_encontrado["nombre"])
            print("Documento: " + cliente_encontrado["documento"])
            print("Vehículo: " + vehiculo_seleccionado["placa"])
            print("Fecha: " + fecha_cita)
            print("Hora: " + hora_cita)

        else:
            print("Opción de vehículo inválida.")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")


cita = {
    "cliente": cliente_encontrado["nombre"],
    "documento": cliente_encontrado["documento"],
    "vehiculo": vehiculo_seleccionado["placa"],
    "fecha": fecha_cita,
    "hora": hora_cita
}

def consultar_citas():
    from citas import citas

    print("----- Mis Citas -----")

    if not citas:
        print("No hay citas programadas.")
        return

    documento = input("Ingrese su documento: ").strip()

    encontrada = False

    for cita in citas:
        if cita["documento"] == documento:
            print()
            print("Cliente: " + cita["cliente"])
            print("Vehículo: " + cita["vehiculo"])
            print("Fecha: " + cita["fecha"])
            print("Hora: " + cita["hora"])
            encontrada = True

    if not encontrada:
        print("No se encontraron citas para este usuario.")
