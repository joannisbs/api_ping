from users.models import HistoryUser

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

        tamanho = len(HistoryUser.objects.filter(
            user_nome__icontains=filter, user_ids=iduser))
        
        res = HistoryUser.objects.filter(
            user_nome__icontains=filter, user_ids=iduser)[number1:number]
        
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
