instructores = []


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
            print("Debe ingresar un nombre.")
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
        print("Instructor registrado: " + nombre)
        break


def consultar_instructores():
    if not instructores:
        print("No hay instructores registrados.")
        return
    print("Instructores registrados:")
    for i, instructor in enumerate(instructores, start=1):
        print(str(i) + ". " + instructor['nombre'] + " - Vehículo: " + instructor['tipo_vehiculo'])
