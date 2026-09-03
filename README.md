#DriveSafe 

By: Camilo Andrès Osorio y Juan Pablo Castro

DriveSafe es una aplicación desarrollada en Python para gestionar las prácticas de conducción de una academia. El sistema funciona desde consola y permite administrar clientes, instructores, vehículos y citas de práctica.

## Funcionalidades

* Registrar y consultar clientes.
* Registrar instructores y su especialidad.
* Registrar vehículos y controlar su disponibilidad.
* Programar citas de práctica.
* Consultar citas por cliente o fecha.
* Registrar asistencia y observaciones.
* Consultar el historial de prácticas de cada cliente.
* Guardar y cargar información mediante archivos locales **JSON/TXT**.

## Estructura del proyecto

```text
DriveSafe/
│
├── main.py
├── clientes.py
├── citas.py
├── instructores.py
├── vehiculos.py
└── archivos/
    └── datos.json

Facilitar la administración de las prácticas de conducción, evitando conflictos de horarios y mejorando el control de clientes, instructores, vehículos, asistencia e historial de prácticas.
