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
        break

    instructores.append({"nombre": nombre})
    print("Instructor registrado: " + nombre)


def consultar_instructores():
    if not instructores:
        print("No hay instructores registrados.")
        return
    print("Instructores registrados:")
    for i, instructor in enumerate(instructores, start=1):
        print(str(i) + ". " + instructor['nombre'])
