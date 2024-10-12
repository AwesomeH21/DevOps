class Cuenta:
    def __init__(self):
        self.balance = 0

    def depositar(self, depositos):
        for deposito in depositos:
            self.balance += deposito
            print(f"Depósito de {deposito} realizado. Balance actual: {self.balance}")

    def balance_actual(self):
        return self.balance

mi_cuenta = Cuenta()

depositos = [100, 200, 50, 25]
mi_cuenta.depositar(depositos)

print(f"Balance final: {mi_cuenta.balance_actual()}")
