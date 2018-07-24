from users.models import User

def getListUsers(page, filter):
    
    number = int(page) * 25
    number1 = number - 25
    
    if filter == "all":
        respo = []
        otherpage = 0
        tamanho = len(User.objects.filter(user_ativo='s'))
        res = User.objects.filter(user_ativo='s').order_by("user_nome")[number1:number]
        if number>tamanho:
            number=tamanho
            otherpage = 1
        respo.append([str(number1+1),str(number),str(tamanho),str(otherpage)])
        for re in res:
            person = [re.id,re.user_nome,re.user_tipe]
            respo.append(person)
        return respo
    else:
        
        respo = []
        otherpage = 0
        tamanho = len(User.objects.filter(user_nome__icontains=filter, user_ativo='s'))
        res = User.objects.filter(user_nome__icontains=filter, user_ativo='s').order_by("user_nome")[number1:number]
        if number>tamanho:
            number=tamanho
            otherpage = 1
        respo.append([str(number1+1),str(number),str(tamanho),str(otherpage)])
        for re in res:
            person = [re.id,re.user_nome,re.user_tipe]
            respo.append(person)
        filter = ''
        return respo
