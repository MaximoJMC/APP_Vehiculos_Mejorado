class Vehiculo:
    contador_vehiculos = 0

    def __init__(self, placa, modelo, color):
        self.id_vehiculo = Vehiculo.contador_vehiculos + 1
        Vehiculo.contador_vehiculos += 1
        self.placa = placa
        self.modelo = modelo
        self.color = color
        self.estado = 0  # Disponible = 0 , No disponible = 1

    def modificar(self, placa=None, modelo=None, color=None):
        if placa:
            self.placa = placa
        if modelo:
            self.modelo = modelo
        if color:
            self.color = color

    def modificar_estado(self, estado):
        self.estado = estado

    @staticmethod
    def listar(vehiculos):
        if vehiculos:
            for vehiculo in vehiculos:
                print(f"ID: {vehiculo.id_vehiculo}, "
                    f"Placa: {vehiculo.placa}, "
                    f"Modelo: {vehiculo.modelo}, "
                    f"Color: {vehiculo.color}, "
                    f"Estado: {'Disponible' if vehiculo.estado == 0 else 'No disponible'}")
        else:
            print("No hay vehículos registrados.")

    @staticmethod
    def crear_vehiculo(vehiculos, placa, modelo, color):
        vehiculo = Vehiculo(placa, modelo, color)
        vehiculos.append(vehiculo)
        print("Vehículo creado exitosamente.")

    @staticmethod
    def consultar_vehiculo(vehiculos, placa):
        return next((v for v in vehiculos if v.placa == placa), None)

    @staticmethod
    def modificar_vehiculo(vehiculos, placa, nuevo_modelo, nuevo_color):
        vehiculo = Vehiculo.consultar_vehiculo(vehiculos, placa)
        if vehiculo:
            vehiculo.modificar(modelo=nuevo_modelo, color=nuevo_color)
            print("Vehículo modificado exitosamente.")
        else:
            print("Vehículo no encontrado.")

    @staticmethod
    def eliminar_vehiculo(vehiculos, placa):
        vehiculo = Vehiculo.consultar_vehiculo(vehiculos, placa)
        if vehiculo:
            vehiculos.remove(vehiculo)
            print("Vehículo eliminado exitosamente.")
        else:
            print("Vehículo no encontrado.")



