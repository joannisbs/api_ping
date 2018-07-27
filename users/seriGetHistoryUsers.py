from users.models import HistoryUser
from django.db.models import Q

def HistoryUsuario(iduser,page, filter):
    number  = int(page) * 50
    number1 = number - 50
    
    if filter == "all":
        respo     = []
        otherpage = 0

        tamanho   = len(HistoryUser.objects.filter(user_ids=iduser))

        res = HistoryUser.objects.filter(user_ids=iduser)[number1:number]

        if number>tamanho:
            number=tamanho
            otherpage = 1

        respo.append([str(number1+1),str(number),str(tamanho),str(otherpage)])
        
        for re in res:
            person = [re.event,re.hora]
            respo.append(person)
        return respo

    else:
        respo = []
        otherpage = 0

        filter = ArrumaData(filter)

        tamanho = len(HistoryUser.objects.filter(Q(
            event__icontains=filter, user_ids=iduser)|
            Q(hora__icontains=filter, user_ids=iduser)))
        

        res = HistoryUser.objects.filter(Q(
            event__icontains=filter, user_ids=iduser)|
            Q(hora__icontains=filter, user_ids=iduser))[number1:number]
        
        if number > tamanho:
            number      = tamanho
            otherpage   = 1

        respo.append([str(number1+1),
            str(number),str(tamanho),str(otherpage)])

        for re in res:
            person = [re.event,re.hora]
            respo.append(person)
            
        filter = ''
        return respo


def ArrumaData(data):
    dataarrumada = data
    if '/' in data:
        dado = data.split('/')
        if len(dado) == 3:
            if len(dado[2])==1:
                dado[2] = ''
            if len(dado[0])==1:
                dado[0] = '0' + dado[0]
            if len(dado[2])==3:
                dado[2] = ''
            if len(dado[2])==4:
                dado[2] = dado[2][2] + dado[2][3]
            dataarrumada = dado[2] + "_" + dado[1] + "_" + dado [0]
        elif len(dado) == 2:
            if len(dado[1])==1:
                dado[1] = ''
            if len(dado[0])==1:
                dado[0] = '0' + dado[0]
            dataarrumada = dado[1] + "_" + dado [0]
        else:
            dataarrumada = data

    return dataarrumada