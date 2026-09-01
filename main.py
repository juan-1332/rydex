
import clientes
import vehiculos


def menu():
    print("-----------------------")
    print("-BIENVENIDO A DRIVESAFE-")
    print("-Sistema De Citas Para Conducccion")
    print("1. registrar cliente")
    print("2. ver clientes registrados")
    print("3. programar citas")
    print("4. controlar asistencia")
    print("5. consultar historial de clientes")
    print("6. registrar instructor")
    print("7. consultar instructores")
    print("8. registrar vehiculo")
    print("9. consultar vehiculos")
    print("10. salir")


while True:
    menu()
    opcion = input("Ingrese una opcion: ").strip()

    if opcion == "1":
        clientes.registrar_cliente()
    elif opcion == "2":
        clientes.ver_clientes()
    elif opcion == "3":
        from citas import programar_cita
        programar_cita()
    elif opcion == "4":
        from asistencia import controlar_asistencia
        controlar_asistencia()
    elif opcion == "5":
        from historial import consultar_historial
        consultar_historial()
    elif opcion == "6":
        from instructores import registrar_instructor
        registrar_instructor()
    elif opcion == "7":
        from instructores import consultar_instructores
        consultar_instructores()
    elif opcion == "8":
        from vehiculos import registrar_vehiculo
        registrar_vehiculo()
    elif opcion == "9":
        vehiculos.consultar_vehiculos()
    elif opcion == "10":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida. Intente nuevamente.")
        input("Presione Enter para continuar...")
