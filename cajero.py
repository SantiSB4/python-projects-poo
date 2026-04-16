class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self,monto):
        if monto > 0:
            self.saldo += monto
            print('Retiro exitoso')
        else:
            print('Monto invalido')
        
    def retirar(self,monto):
        if monto <= self.saldo and monto > 0:
            self.saldo -= monto
            print('Retiro exitoso')
        else:
            print('Fondos insuficientes')
            
    def __str__(self):
        return f'Titular: {self.titular} | Saldo: ${self.saldo}'
    
nombre = input('Ingrese el nombre del titular: ')
saldo_inicial = float(input('Ingrese el saldo inicial: '))

cuenta = CuentaBancaria(nombre,saldo_inicial)

#Menu tipo cajero automatico

while True:
    print("\n---CAJERO AUTOMATICO---")
    print("1.Ver cuenta")
    print("2.Depositar")
    print("3.Retirar")
    print("4.Salir")
    
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print(cuenta)
    
    elif opcion == "2":
        monto = float(input("Monto a depositar: "))
        cuenta.depositar(monto)

    elif opcion == "3":
        monto = float(input("Monto a retirar: "))
        cuenta.retirar(monto)

    elif opcion == "4":
        print("Gracias por usar el cajero")
        break

    else:
        print("Opción inválida")

       
    