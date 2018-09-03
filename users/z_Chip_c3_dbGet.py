from users.models import Chip, EntradaChipEstoque

from z_User_c0_obj import Get_ListUsersSizeObject
from z_Chip_c0_obj import db_ChipObject , Resp_ChipDateGenericObject
from django.db.models import Q

def Get_CheckChipNumberNotExists(number):
    try:
        Chips =  Chip.objects.filter(chip_num = number)
        # Existe Apenas um usuario com este nome no banco. 
        for chip in Chips:
            chip.number = '=)'
            return False
        return True
    except:
        return True

def Get_CheckChipIpAdressNotExists(IpAdress):
    if IpAdress == 'host':
        return True
    try:
        Chips =  Chip.objects.filter(chip_ip = IpAdress)
        # Existe Apenas um usuario com este nome no banco. 
        for chip in Chips:
            chip.IpAdress = '=)'
            return False
        return True
    except:
        return True

def Get_ChipIDbychipNumber(number):
    try:
        Chips =  Chip.objects.filter(chip_num = number)
        # Existe Apenas um usuario com este nome no banco. 
        for chip in Chips:
            return chip.id
        return False
    except:
        return False

def Get_ChilListSize (pagina,search,categ,ativo):
    fimPaginacao  = int(pagina) * 50
    initPaginacao = fimPaginacao - 50

    if categ == 'all':
        if search == 'all':
            sizeofListofChips = len(Chip.objects.filter(chip_ativo=ativo))
                
        else:
            sizeofListofChips = len(Chip.objects.filter(
                Q( chip_data__icontains =search ,chip_ativo=ativo)|
                Q( chip_ip__icontains   =search ,chip_ativo=ativo)|
                Q( chip_num__icontains  =search ,chip_ativo=ativo)|
                Q( chip_oper__icontains =search ,chip_ativo=ativo)))

    else:
        if search == 'all':
            sizeofListofChips = len(Chip.objects.filter(chip_where=categ,chip_ativo=ativo))
                
        else:
            sizeofListofChips = len(Chip.objects.filter(
                Q(chip_where=categ, chip_data__icontains =search ,chip_ativo=ativo)|
                Q(chip_where=categ, chip_ip__icontains   =search ,chip_ativo=ativo)|
                Q(chip_where=categ, chip_num__icontains  =search ,chip_ativo=ativo)|
                Q(chip_where=categ, chip_oper__icontains =search ,chip_ativo=ativo)))

    toBeNext = 0

    if fimPaginacao  > sizeofListofChips:
        fimPaginacao = sizeofListofChips
        toBeNext = 1
    response = Get_ListUsersSizeObject()
    response.initpag = initPaginacao
    response.endpag  = fimPaginacao
    response.size    = sizeofListofChips
    response.next    = toBeNext
    return response

def Get_ListChip (pagina,search,categ,ativo):
    fimPaginacao  = int(pagina) * 50
    initPaginacao = fimPaginacao - 50
    ToBeSearch = False

    if categ == 'all':
        if search == 'all':
            resultChipSearch = (Chip.objects.filter(chip_ativo=ativo))
                
        else:
            resultChipSearch = (Chip.objects.filter(
                Q( chip_data__icontains =search ,chip_ativo=ativo)|
                Q( chip_ip__icontains   =search ,chip_ativo=ativo)|
                Q( chip_num__icontains  =search ,chip_ativo=ativo)|
                Q( chip_oper__icontains =search ,chip_ativo=ativo)))

    else:
        if search == 'all':
            resultChipSearch = (Chip.objects.filter(chip_where=categ,chip_ativo=ativo))
                
        else:
            resultChipSearch = (Chip.objects.filter(
                Q(chip_where=categ, chip_data__icontains =search ,chip_ativo=ativo)|
                Q(chip_where=categ, chip_ip__icontains   =search ,chip_ativo=ativo)|
                Q(chip_where=categ, chip_num__icontains  =search ,chip_ativo=ativo)|
                Q(chip_where=categ, chip_oper__icontains =search ,chip_ativo=ativo)))

        
    response = []
    for item in resultChipSearch:
        ToBeSearch = True

        chips                = db_ChipObject()
        chips.id             = item.id
        chips.chip_ip        = item.chip_ip
        chips.chip_num       = item.chip_num
        chips.chip_oper      = item.chip_oper
        chips.chip_data      = item.chip_data
        chips.chip_ativo     = item.chip_ativo
        chips.chip_where     = item.chip_where
        chips.chip_whedes    = item.chip_whedes
        response.append(chips)
    if ToBeSearch:
        return response
    return False

def Get_estoqueByChipID(ChipID):
    resultChipSearch = (EntradaChipEstoque.objects.filter(chip_id=ChipID).order_by('-id'))
    resp = Resp_ChipDateGenericObject()
    for item in resultChipSearch:
        resp.one = item.chip_data
        resp.two = item.event
        resp.three = item.entradapor
        return resp
        

def Get_SaidaByID(id):
    return "saida"

