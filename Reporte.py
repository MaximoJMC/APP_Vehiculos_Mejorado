from Vehiculo import Vehiculo
from Alquiler import Alquiler

class Reporte:
    @staticmethod
    def consultar_vehiculos(vehiculos):
        Vehiculo.listar(vehiculos)

    @staticmethod
    def consultar_alquileres(alquileres):
        Alquiler.listar(alquileres)

    @staticmethod
    def consultar_servicios(servicios):
        if servicios:
            for servicio in servicios:
                print(f"Código: {servicio.codigo}, "
                    f"Vehículo: {servicio.vehiculo.modelo}, "
                    f"Fecha: {servicio.fecha}, "
                    f"Tipo: {servicio.tipo}, "
                    f"Detalle: {servicio.detalle}")
        else:
            print("No hay servicios registrados.")


    @staticmethod
    def consultar_vehiculos_pendientes(alquileres):
        vehiculos_no_devueltos = [alquiler for alquiler in alquileres if alquiler.estado == 0]
        if vehiculos_no_devueltos:
            for alquiler in vehiculos_no_devueltos:
                print(f"Cliente: {alquiler.cliente.nombres} {alquiler.cliente.apellidos}, "
                    f"Vehículo: {alquiler.vehiculo.modelo}, "
                    f"Fecha: {alquiler.fecha}, "
                    f"Días: {alquiler.dias}, "
                    f"Total: {alquiler.total}")
        else:
            print("No hay vehículos pendientes de devolución.")




            