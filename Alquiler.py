from datetime import datetime
from Vehiculo import Vehiculo
from Cliente import Cliente

class Alquiler:
    contador_alquileres = 0

    def __init__(self, cliente, vehiculo, dias):
        self.codigo = Alquiler.contador_alquileres + 1
        Alquiler.contador_alquileres += 1
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.dias = dias
        self.total = 0.0
        self.estado = 0  # Pendiente = 0 , Devuelto = 1

    def calcular_total(self, precio_por_dia):
        self.total = self.dias * precio_por_dia

    @staticmethod
    def listar(alquileres):
        if alquileres:
            for alquiler in alquileres:
                print(f"Código: {alquiler.codigo}, "
                    f"Cliente: {alquiler.cliente.nombres} {alquiler.cliente.apellidos}, "
                    f"Vehículo: {alquiler.vehiculo.modelo}, "
                    f"Fecha: {alquiler.fecha}, "
                    f"Días: {alquiler.dias}, "
                    f"Total: {alquiler.total}, "
                    f"Estado: {'Pendiente' if alquiler.estado == 0 else 'Devuelto'}")
        else:
            print("No hay alquileres registrados.")

    @staticmethod
    def realizar_alquiler(alquileres, clientes, vehiculos, dni_cliente, placa_vehiculo, dias, precio_por_dia):
        cliente = Cliente.consultar_cliente(clientes, dni_cliente)
        if cliente:
            vehiculo = Vehiculo.consultar_vehiculo(vehiculos, placa_vehiculo)
            if vehiculo and vehiculo.estado == 0:
                alquiler = Alquiler(cliente, vehiculo, dias)
                alquiler.calcular_total(precio_por_dia)
                alquileres.append(alquiler)
                vehiculo.modificar_estado(1)
                print("Alquiler registrado exitosamente.")
            else:
                print("Vehículo no disponible.")
        else:
            print("Cliente no encontrado.")

    @staticmethod
    def realizar_pago(alquileres, codigo_alquiler):
        alquiler = next((a for a in alquileres if a.codigo == codigo_alquiler and a.estado == 0), None)
        if alquiler:
            print(f"Total a pagar: {alquiler.total}")
            confirmar = input("Confirme el pago (s/n): ")
            if confirmar.lower() == 's':
                alquiler.estado = 1
                alquiler.vehiculo.modificar_estado(0)
                print("Pago realizado exitosamente.")
            else:
                print("Pago cancelado.")
        else:
            print("Alquiler no encontrado o ya pagado.")


