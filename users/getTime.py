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

    def get_full_db(self):
            #[18_06_04]10h12
        date = ("["+str(self.year)[2] +
                    str(self.year)[3]+"_" +
                str(self.mes).zfill(2)+"_" +
                str(self.day).zfill(2)+"]" +
                str(self.hora).zfill(2)+"h" +
                str(self.minuto).zfill(2))
        return date
        
