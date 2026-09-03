import json


clientes = []


def documento_ya_registrado(documento):
    documento = documento.strip()
    for cliente in clientes:
        if cliente["documento"] == documento:
            return True
    return False


def registrar_cliente():
    while True:
        nombre = input("Ingrese el nombre del cliente: recuerda que al ingresar un cliente ingresalo con nombre y apellido, para evitar confusiones): ").strip()
        if not nombre:
            print("El nombre no puede estar vacio.")
            continue

        break

    while True:
        documento = input("Ingrese el documento del cliente: ").strip()
        if not documento:
            print("El documento no puede estar vacio.")
            continue
        if not documento.isdigit():
            print("El documento debe ser un numero. Ingrese un documento valido.")
            continue

        if documento_ya_registrado(documento):
            print("Ese documento ya existe en el sistema. Ingrese uno diferente.")
            continue

        break

    while True:
        tipo_vehiculo = input("Ingrese el tipo de vehiculo que desea aprender a conducir (moto, carro o ambos): ").strip().lower()
        if tipo_vehiculo in {"moto", "carro", "ambos"}:
            break
        print("Tipo de vehiculo no valido. Use: moto, carro o ambos.")

    cliente = {
        "nombre": nombre,
        "documento": documento,
        "tipo_vehiculo": tipo_vehiculo,
    }
    clientes.append(cliente)
    with open("clientes.json", "w") as archivo:
        json.dump(clientes, archivo, indent=4)
    print("Cliente registrado correctamente: " + nombre)
    return cliente


def ver_clientes():
    if not clientes:
        print("No hay clientes registrados.")
        return

    print("\nClientes registrados:")
    for indice, cliente in enumerate(clientes, start=1):
        print(str(indice) + ". " + cliente['nombre'] + " - Documento: " + cliente['documento'] + " - Vehiculo: " + cliente['tipo_vehiculo'])


with open("clientes.json", "w") as archivo:
    json.dump(clientes, archivo, indent=4)