class Cliente:
    contador_clientes = 0

    def __init__(self, nombres, apellidos, telefono, dni):
        self.codigo = Cliente.contador_clientes + 1
        Cliente.contador_clientes += 1
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.dni = dni

    def modificar(self, nombres=None, apellidos=None, telefono=None):
        if nombres:
            self.nombres = nombres
        if apellidos:
            self.apellidos = apellidos
        if telefono:
            self.telefono = telefono

    @staticmethod
    def listar(clientes):
        if clientes:
            for cliente in clientes:
                print(f"Código: {cliente.codigo}, "
                    f"Nombres: {cliente.nombres}, "
                    f"Apellidos: {cliente.apellidos}, "
                    f"Teléfono: {cliente.telefono}, "
                    f"DNI: {cliente.dni}")
        else:
            print("No hay clientes registrados.")


    @staticmethod
    def crear_cliente(clientes, nombres, apellidos, telefono, dni):
        cliente = Cliente(nombres, apellidos, telefono, dni)
        clientes.append(cliente)
        print("Cliente creado exitosamente.")

    @staticmethod
    def consultar_cliente(clientes, dni):
        return next((c for c in clientes if c.dni == dni), None)

    @staticmethod
    def modificar_cliente(clientes, dni, nuevos_nombres, nuevos_apellidos, nuevo_telefono):
        cliente = Cliente.consultar_cliente(clientes, dni)
        if cliente:
            cliente.modificar(nombres=nuevos_nombres, apellidos=nuevos_apellidos, telefono=nuevo_telefono)
            print("Cliente modificado exitosamente.")
        else:
            print("Cliente no encontrado.")

    @staticmethod
    def eliminar_cliente(clientes, dni):
        cliente = Cliente.consultar_cliente(clientes, dni)
        if cliente:
            clientes.remove(cliente)
            print("Cliente eliminado exitosamente.")
        else:
            print("Cliente no encontrado.")
