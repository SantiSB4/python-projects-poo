class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
        
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad 

class Auto():
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
        
    #Creando una funcion para mover el auto
    def mover(self,distancia):
        
         #Cada dos de distancia gastamos uno de combustible
        if self.tanque.obtener_combustible() >= distancia / 2: 
            
            #Aqui hacemos que su posicion sea igual a la distancia que recorrio
            self.posicion += distancia 
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")
            
    #creando un metodo para que nos devuelva la posicion del auto
    def obtener_posicion(self):
        return self.posicion
                  

tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
print(autito.mover(10))
print(autito.obtener_posicion())
print(autito.mover(20))
print(autito.obtener_posicion())
print(autito.mover(60))
print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())
        
#Volver a ver este tema

 
    
    
    