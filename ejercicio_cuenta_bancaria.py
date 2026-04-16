#Crear una clase llamada CuentaBancaria
class CuentaBancaria:
    
#Atributos: titular, saldo(inicia en 0)
    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0

#Metodos depositar(monto): Suma el monto al saldo, no permite valores negativos 
    def depositar(self,monto):
        if monto > 0:
            self.saldo += monto
            print(f"Deposito exitoso! ${monto}")
        else:
            print("El monto debe ser positivo")
            
#Metodo retirar(monto): resta el monto al saldo, no permite retirar mas del saldo 
    def retirar(self,monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        elif monto <= 0:
            print("El monto debe ser positivo")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso: ${self.saldo}")
            
#Metodo mostrar_saldo(): muestra el saldo actual 
    def mostrar_saldo(self):
        print(f"Saldo actual: ${self.saldo}")
        
#Usar la clase
cuenta = CuentaBancaria("Santiago")

cuenta.mostrar_saldo()
cuenta.depositar(1000000)
cuenta.retirar(5000)
cuenta.mostrar_saldo()
