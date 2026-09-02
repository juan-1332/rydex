def programar_cita():
    from clientes import clientes
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
    print("Vehículos registrados para este cliente:")
    vehiculos_cliente = [v for v in vehiculos if v["cliente"] == cliente_encontrado["nombre"]]

    if not vehiculos_cliente:
        print("No hay vehículos registrados para este cliente. Por favor, registre un vehículo primero.")
        return

    for idx, vehiculo in enumerate(vehiculos_cliente, start=1):
        print(str(idx) + ". Placa: " + vehiculo["placa"] + ", Modelo: " + vehiculo["modelo"])

    opcion_vehiculo = input("Seleccione el número del vehículo para la cita: ").strip()
    
    try:
        opcion_vehiculo = int(opcion_vehiculo)
        if 1 <= opcion_vehiculo <= len(vehiculos_cliente):
            vehiculo_seleccionado = vehiculos_cliente[opcion_vehiculo - 1]
            fecha_cita = input("Ingrese la fecha de la cita (YYYY-MM-DD): ").strip()
            hora_cita = input("Ingrese la hora de la cita (HH:MM): ").strip()
            print("Cita programada para " + cliente_encontrado["nombre"] + " con el vehículo " + vehiculo_seleccionado["placa"] + " el " + fecha_cita + " a las " + hora_cita + ".")
        else:
            print("Opción de vehículo inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
    
