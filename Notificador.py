class Notificador():
    def __init__(self, usurario, mensaje):
        self.usurario = usurario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por MAIL a {self.usurario.email}')
        
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f'Enviando SMS a {self.usurario.sms}')
        
        
class NotificadorWhatsapp(Notificador):
    def Notificar(self):
        print(f'Enviando Whatsapp a {self.usurario.whatsapp}')
        
        
class NotificadorX(Notificador):
    def Notificar(self):
        print(f'Enviando X a {self.usurario.X}')
        

        