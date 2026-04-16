from abc import ABC, abstractmethod

class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass
    
class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
class Duermiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass
 

class Humano(Trabajador, Comedor, Duermiente):
    
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("El humano esta trabajando")
    
    def dormir(self):
        print("El humano esta durmiendo")
    

class Robot(Trabajador):
    def comer(self):
        pass
    
    def trabajar(self):
        print("El robot esta trabajando")
        
    def dormir(self):
        pass
        
        
robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()



