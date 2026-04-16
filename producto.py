class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self._precio = precio #Atributo privado
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,nuevo_precio):
        if nuevo_precio < 0:
            print("Error: el precio no puede ser negativo")
        else:
            self._precio = nuevo_precio
            
            # -------- DESCUENTO --------
    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, nuevo_descuento):
        if 0 <= nuevo_descuento <= 50:
            self._descuento = nuevo_descuento
        else:
            print("Error: el descuento debe estar entre 0 y 50")
        
#Prueba
p1 = Producto("Audifonos", 100)
print(p1.precio)

p1.descuento = 20
print(p1.descuento)

p1.descuento = 70
print(p1.descuento)