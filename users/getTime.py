from datetime import datetime

class GetTime(object):
    
    def __init__(self):
        now = datetime.now()
        self.hora = now.hour
        self.minuto = now.minute
        self.segundo = now.second
        self.day = now.day
        self.mes = now.month
        self.year = now.year


    def get_TimeInMinuts(self):
        AnoBase = 2015
        Cotage = self.year - AnoBase
        Cotage = Cotage * 12
        Cotage = Cotage + self.mes
        Cotage = Cotage * 31
        Cotage = Cotage + self.day
        Cotage = Cotage * 24
        Cotage = Cotage + self.hora
        Cotage = Cotage * 60
        Cotage = Cotage + self.minuto
        return Cotage