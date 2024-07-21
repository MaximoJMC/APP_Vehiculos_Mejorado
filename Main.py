from Vehiculo import Vehiculo
from Cliente import Cliente
from Conductor import Conductor
from Alquiler import Alquiler
from Reporte import Reporte

def menu_principal():
    vehiculos = []
    conductores = []
    clientes = []
    alquileres = []
    servicios = []

    while True:
        print("\n--- Menú Principal ---")
        print("1. Mantenimiento de vehículos")
        print("2. Mantenimiento de conductores")
        print("3. Mantenimiento de clientes")
        print("4. Registro de alquileres")
        print("5. Realizar pagos")
        print("6. Reportes")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                print("\n--- Mantenimiento de Vehículos ---")
                print("1. Crear vehículo")
                print("2. Modificar vehículo")
                print("3. Eliminar vehículo")
                print("4. Consultar vehículos")
                print("5. Volver al menú principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "1":
                    placa = input("Ingrese la placa del vehículo: ")
                    modelo = input("Ingrese el modelo del vehículo: ")
                    color = input("Ingrese el color del vehículo: ")
                    Vehiculo.crear_vehiculo(vehiculos, placa, modelo, color)
                elif sub_opcion == "2":
                    placa = input("Ingrese la placa del vehículo a modificar: ")
                    nuevo_modelo = input("Ingrese el nuevo modelo: ")
                    nuevo_color = input("Ingrese el nuevo color: ")
                    Vehiculo.modificar_vehiculo(vehiculos, placa, nuevo_modelo, nuevo_color)
                elif sub_opcion == "3":
                    placa = input("Ingrese la placa del vehículo a eliminar: ")
                    Vehiculo.eliminar_vehiculo(vehiculos, placa)
                elif sub_opcion == "4":
                    Vehiculo.listar(vehiculos)
                elif sub_opcion == "5":
                    break
                else:
                    print("Opción no válida, intente nuevamente.")

        elif opcion == "2":
            while True:
                print("\n--- Mantenimiento de Conductores ---")
                print("1. Crear conductor")
                print("2. Modificar conductor")
                print("3. Eliminar conductor")
                print("4. Consultar conductores")
                print("5. Volver al menú principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "1":
                    nrobrevete = input("Ingrese el número de brevete: ")
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    categoria = input("Ingrese la categoría: ")
                    Conductor.crear_conductor(conductores, nrobrevete, nombre, apellido, categoria)
                elif sub_opcion == "2":
                    nrobrevete = input("Ingrese el número de brevete del conductor a modificar: ")
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    nuevo_apellido = input("Ingrese el nuevo apellido: ")
                    nueva_categoria = input("Ingrese la nueva categoría: ")
                    Conductor.modificar_conductor(conductores, nrobrevete, nuevo_nombre, nuevo_apellido, nueva_categoria)
                elif sub_opcion == "3":
                    nrobrevete = input("Ingrese el número de brevete del conductor a eliminar: ")
                    Conductor.eliminar_conductor(conductores, nrobrevete)
                elif sub_opcion == "4":
                    Conductor.listar(conductores)
                elif sub_opcion == "5":
                    break
                else:
                    print("Opción no válida, intente nuevamente.")

        elif opcion == "3":
            while True:
                print("\n--- Mantenimiento de Clientes ---")
                print("1. Crear cliente")
                print("2. Modificar cliente")
                print("3. Eliminar cliente")
                print("4. Consultar clientes")
                print("5. Volver al menú principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "1":
                    nombres = input("Ingrese los nombres del cliente: ")
                    apellidos = input("Ingrese los apellidos del cliente: ")
                    telefono = input("Ingrese el teléfono del cliente: ")
                    dni = input("Ingrese el DNI del cliente: ")
                    Cliente.crear_cliente(clientes, nombres, apellidos, telefono, dni)
                elif sub_opcion == "2":
                    dni = input("Ingrese el DNI del cliente a modificar: ")
                    nuevos_nombres = input("Ingrese los nuevos nombres: ")
                    nuevos_apellidos = input("Ingrese los nuevos apellidos: ")
                    nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                    Cliente.modificar_cliente(clientes, dni, nuevos_nombres, nuevos_apellidos, nuevo_telefono)
                elif sub_opcion == "3":
                    dni = input("Ingrese el DNI del cliente a eliminar: ")
                    Cliente.eliminar_cliente(clientes, dni)
                elif sub_opcion == "4":
                    Cliente.listar(clientes)
                elif sub_opcion == "5":
                    break
                else:
                    print("Opción no válida, intente nuevamente.")

        elif opcion == "4":
            dni_cliente = input("Ingrese el DNI del cliente: ")
            placa_vehiculo = input("Ingrese la placa del vehículo: ")
            dias = int(input("Ingrese la cantidad de días: "))
            precio_por_dia = float(input("Ingrese el precio por día: "))
            Alquiler.realizar_alquiler(alquileres, clientes, vehiculos, dni_cliente, placa_vehiculo, dias, precio_por_dia)

        elif opcion == "5":
            codigo_alquiler = int(input("Ingrese el código del alquiler a pagar: "))
            Alquiler.realizar_pago(alquileres, codigo_alquiler)

        elif opcion == "6":
            while True:
                print("\n--- Reportes ---")
                print("1. Consultar vehículos")
                print("2. Consultar alquileres")
                print("3. Consultar servicios")
                print("4. Consultar vehículos pendientes de devolución")
                print("5. Volver al menú principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "1":
                    Reporte.consultar_vehiculos(vehiculos)
                elif sub_opcion == "2":
                    Reporte.consultar_alquileres(alquileres)
                elif sub_opcion == "3":
                    Reporte.consultar_servicios(servicios)
                elif sub_opcion == "4":
                    Reporte.consultar_vehiculos_pendientes(alquileres)
                elif sub_opcion == "5":
                    break
                else:
                    print("Opción no válida, intente nuevamente.")

        elif opcion == "7":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción no válida, intente nuevamente.")


menu_principal()