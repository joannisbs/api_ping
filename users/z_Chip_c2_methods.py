
# import methodos dos usuarios
from z_User_c3_dbGet import Get_UserById
from z_User_c2_methods import InsertHistoryUser
from z_User_c2_methods import GetTimeDB
from z_User_c2_modals import SizeListUser_Serializer

from z_Chip_c0_obj import Post_historyChipObject 
from z_Chip_c0_obj import EstoqueChip

from z_Chip_c2_modals import ResponseNewChip_Modal , ResponseChipDateGeneric_Serializer
from z_Chip_c2_modals import Chip_Serializer

from z_Chip_c3_dbGet import Get_CheckChipIpAdressNotExists
from z_Chip_c3_dbGet import Get_CheckChipNumberNotExists
from z_Chip_c3_dbGet import Get_ChipIDbychipNumber
from z_Chip_c3_dbGet import Get_ChilListSize 
from z_Chip_c3_dbGet import Get_ListChip 
from z_Chip_c3_dbGet import Get_estoqueByChipID 
from z_Chip_c3_dbGet import Get_ChipNumberbyChipId
#from z_Chip_c3_dbGet import Get_SaidaByIp

from z_Chip_c3_dbUpdt import Updt_DeleteChip 
from z_Chip_c3_dbUpdt import Updt_ActiveChip 
from z_Chip_c3_dbUpdt import Updt_EditIpChip 

from z_Chip_c3_dbPost import Post_CreateChip
from z_Chip_c3_dbPost import Post_ChipHistoryDbSeri 
from z_Chip_c3_dbPost import Post_ChipToEstoque

from z__functionsgenericas import ArrumaData

from z_User_c2_modals import S_StandardResponse_Modal 

def CreateChip_method(id_user, chip):
     # 1 Chip Existente
     # 2 Conflito de Ip
     # 3 dados Inconsistentes
    if Get_CheckChipNumberNotExists(chip.chip_num):
        if Get_CheckChipIpAdressNotExists(chip.chip_ip):
            chipser = Post_CreateChip(chip)
            if chipser.Save(chipser.data):
                ResponseNewChip_Modal(chip,True,'0')
                iddochip = Get_ChipIDbychipNumber(chip.chip_num)
                name = Get_UserById(int(id_user) )
                InsertHistoryUser(id_user,"Cadastrou o chip: "+ chip.chip_num + " ip: " + chip.chip_ip)
                InsertHistoryChip(iddochip,"Chip: "+ chip.chip_num + 
                                            " ip: " + chip.chip_ip + 
                                            " cadastrado por: " + name)

                InsertChipToEstoque(iddochip,name,"Chip novo")

                return ResponseNewChip_Modal(chip,True,'0')
            else:
                return ResponseNewChip_Modal(chip,False,'3')
        else:
            return ResponseNewChip_Modal(chip,False,'2')
    else:
        return ResponseNewChip_Modal(chip,False,'1')
    return ResponseNewChip_Modal(chip,False,'3')

def ListChip_Method(pagina,search,categ,active):
    categ = GetCodeOfCatg(categ)
    response = []
    try:
        sizeof = Get_ChilListSize(pagina, search,categ,active)
        sizeof = SizeListUser_Serializer(sizeof)
        sizeof = sizeof.data
        
        listChip = Get_ListChip(pagina, search,categ,active)
        
        listofChipsSerializada = []
        listofdados = []
        for item in listChip:
            chips = Chip_Serializer(item)
            listofChipsSerializada.append(chips.data)
   
            if item.chip_where == 'e':
                dados = Get_estoqueByChipID(item.id)
                dados = ResponseChipDateGeneric_Serializer(dados)
                listofdados.append(dados.data)
        response.append(sizeof)
        response.append(listofChipsSerializada)
        response.append(listofdados)
        return response

    except:
        
        return S_StandardResponse_Modal(False,0)
    return 0
    
def DeletChip_method(chipid,idsuser,motivo):
    try:
        Updt_DeleteChip(chipid)
        name = Get_UserById(int(idsuser) )
        number = Get_ChipNumberbyChipId(int(chipid))
        InsertHistoryChip(chipid,"Chip deletado por " + name + ", motivo " + motivo)
        InsertHistoryUser(idsuser,"Deletou o chip: "+ number + ", motivo " + motivo)
        return True
    except:
        return False

def EditIpChip_method(chipid,chipip,chipoper,idsuser, motivo):
    try:
        Updt_EditIpChip(chipid,chipip,chipoper)
        name = Get_UserById(int(idsuser) )
        number = Get_ChipNumberbyChipId(int(chipid))
        InsertHistoryChip(chipid,"Ip Alterado por " + name + ", para " + chipip + " " + motivo)
        InsertHistoryUser(idsuser,"Alterou o ip do chip: "+ number + ",para " + chipip + " motivo " + motivo)
        return True
    except:
        return False


def ActivChip_method(chipid,idsuser,motivo):
    try:
        Updt_ActiveChip(chipid)
        name = Get_UserById(int(idsuser) )
        number = Get_ChipNumberbyChipId(int(chipid))
        InsertHistoryChip(chipid,"Chip Reativado por " + name + ", motivo " + motivo)
        InsertHistoryUser(idsuser,"Reativou o chip: "+ number + ", motivo " + motivo)
        return True
    except:
        return False

def InsertChipToEstoque(idchip,user,event):
    entradaestoque = EstoqueChip()
    time = GetTimeDB()
    entradaestoque.chip_data = time
    entradaestoque.chip_id = idchip
    entradaestoque.entradapor = user
    entradaestoque.event = event
    entradaestoque = Post_ChipToEstoque(entradaestoque)
    entradaestoque.Save(entradaestoque.data)

def InsertHistoryChip(chips_ids,hystory):
    histo = Post_historyChipObject()
    time = GetTimeDB()
    histo.chip_id = int(chips_ids)
    histo.hora = time
    histo.event = hystory
    histo = Post_ChipHistoryDbSeri(histo)
    histo.Save(histo.data)

def GetCodeOfCatg ( categoria ):
    if categoria == "Todos":
        categoria = "all"
    elif categoria == "Estoque":
        categoria = 'e'
    elif categoria == "Funcionamento":
        categoria = 'f'
    elif categoria == "Saida":
        categoria = 's'  
    return categoria



