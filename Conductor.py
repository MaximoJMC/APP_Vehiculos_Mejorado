class Conductor:
    contador_conductores = 0

    def __init__(self, nro_brevete, nombre, apellido, categoria):
        self.id_conductor = Conductor.contador_conductores + 1
        Conductor.contador_conductores += 1
        self.nro_brevete = nro_brevete
        self.nombre = nombre
        self.apellido = apellido
        self.categoria = categoria

    def modificar(self, nombre=None, apellido=None, categoria=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if categoria:
            self.categoria = categoria

    @staticmethod
    def listar(conductores):
        if conductores:
            for conductor in conductores:
                print(f"ID: {conductor.id_conductor}, "
                    f"Brevete: {conductor.nro_brevete}, "
                    f"Nombre: {conductor.nombre}, "
                    f"Apellido: {conductor.apellido}, "
                    f"Categoría: {conductor.categoria}")
        else:
            print("No hay conductores registrados.")


    @staticmethod
    def crear_conductor(conductores, nro_brevete, nombre, apellido, categoria):
        conductor = Conductor(nro_brevete, nombre, apellido, categoria)
        conductores.append(conductor)
        print("Conductor creado exitosamente.")

    @staticmethod
    def consultar_conductor(conductores, nro_brevete):
        return next((c for c in conductores if c.nro_brevete == nro_brevete), None)

    @staticmethod
    def modificar_conductor(conductores, nro_brevete, nuevo_nombre, nuevo_apellido, nueva_categoria):
        conductor = Conductor.consultar_conductor(conductores, nro_brevete)
        if conductor:
            conductor.modificar(nombre=nuevo_nombre, apellido=nuevo_apellido, categoria=nueva_categoria)
            print("Conductor modificado exitosamente.")
        else:
            print("Conductor no encontrado.")

    @staticmethod
    def eliminar_conductor(conductores, nro_brevete):
        conductor = Conductor.consultar_conductor(conductores, nro_brevete)
        if conductor:
            conductores.remove(conductor)
            print("Conductor eliminado exitosamente.")
        else:
            print("Conductor no encontrado.")
