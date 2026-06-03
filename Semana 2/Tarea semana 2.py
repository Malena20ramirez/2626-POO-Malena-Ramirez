class CuentaBancaria:
    """
    Clase que representa una Cuenta Bancaria del mundo real.
    Cumple con los principios básicos de la Programación Orientada a Objetos.
    """

    # 1. ATRIBUTOS (Definidos en el constructor)
    def __init__(self, titular, numero_cuenta, saldo_inicial=0.0):
        self.titular = titular  # Atributo 1: Nombre del dueño
        self.numero_cuenta = numero_cuenta  # Atributo 2: Identificador único
        self.saldo = saldo_inicial  # Atributo 3: Dinero disponible

    # 2. MÉTODOS (Acciones que puede realizar la clase)

    # Método 1: Depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(self.saldo)
            print(f"--- Depósito exitoso en la cuenta de {self.titular} ---")
            print(f"Monto depositado: ${cantidad:.2f}")
            print(f"Saldo actual: ${self.saldo:.2f}\n")
        else:
            print("Error: El monto a depositar debe ser mayor a cero.\n")

    # Método 2: Retirar dinero
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"--- Intento de retiro fallido ---")
            print(f"Error: Fondos insuficientes en la cuenta de {self.titular}.\n")
        elif cantidad <= 0:
            print("Error: El monto a retirar debe ser mayor a cero.\n")
        else:
            self.saldo -= cantidad
            print(f"--- Retiro exitoso de la cuenta de {self.titular} ---")
            print(f"Monto retirado: ${cantidad:.2f}")
            print(f"Saldo restante: ${self.saldo:.2f}\n")

    # Método extra para mostrar el estado de la cuenta de forma ordenada
    def mostrar_informacion(self):
        print(f"====== INFORMACIÓN DE LA CUENTA ======")
        print(f"Titular: {self.titular}")
        print(f"Nº de Cuenta: {self.numero_cuenta}")
        print(f"Saldo Disponible: ${self.saldo:.2f}")
        print(f"======================================\n")


# 3. CREACIÓN Y USO DE OBJETOS (Instancias)

# Objeto 1: Cuenta de Carlos Ramirez con un saldo inicial de $500
cuenta_carlos = CuentaBancaria("Carlos Ramirez", "1723456789", 500.0)

# Objeto 2: Cuenta de Ana López con un saldo inicial de $100
cuenta_ana = CuentaBancaria("Ana López", "0987654321", 100.0)

# --- Demostración del funcionamiento ---
print("INICIANDO OPERACIONES BANCARIAS...\n")

# Operaciones con el Objeto 1
cuenta_carlos.mostrar_informacion()
cuenta_carlos.depositar(150.50)
cuenta_carlos.retirar(200.00)

# Operaciones con el Objeto 2
cuenta_ana.mostrar_informacion()
cuenta_ana.retirar(150.00)  # Esto generará un error de fondos insuficientes
cuenta_ana.depositar(80.00)