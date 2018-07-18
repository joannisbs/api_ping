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
        Cotage = str(self.day).zfill(2)
        Cotage = int(Cotage) * 24
        Cotage = Cotage + int(str(self.hora).zfill(2))
        Cotage = Cotage * 60
        Cotage = Cotage + int(str(self.minuto).zfill(2))
        return str(Cotage).zfill(6)