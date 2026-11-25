# clase cuenta con los atributos: numero_cuenta, saldo, tipo_cuenta
class Cuenta:
    def __init__(self, numero_cuenta, saldo, tipo_cuenta):
        #atributos privados
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__tipo_cuenta = tipo_cuenta

    def retirar(self, cantidad) -> bool:
        if cantidad > self.saldo:
            print("Saldo insuficiente")
            return False
        self.saldo -= cantidad
        self.registrar_transaccion(f"Retiro de {cantidad} a la cuenta {self.numero_cuenta}")
        return True


    def registrar(self, transaccion) -> None:
        print(f"La cuenta {self.numero_cuenta} ha realizado la transaccion: {transaccion}")
        self.transacciones.append(transaccion)

# metodos getter y setter
    def set_saldo(self, saldo) -> None:
        self.saldo = saldo

    def set_numero_cuenta(self, numero_cuenta) -> None:
        self.numero_cuenta = numero_cuenta

    def set_tipo_cuenta(self, tipo_cuenta) -> None:
        self.tipo_cuenta = tipo_cuenta

    def get_transacciones(self) -> list:
        return self.transacciones

    def get_saldo(self) -> float:   
        return self.saldo

    def get_numero_cuenta(self) -> str:
        return self.numero_cuenta

    def get_tipo_cuenta(self) -> str:
        return self.tipo_cuenta