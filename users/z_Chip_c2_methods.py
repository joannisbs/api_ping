# import methodos dos usuarios
from z_User_c3_dbGet import Get_UserById
from z_User_c2_methods import InsertHistoryUser


from z_Chip_c2_modals import ResponseNewChip_Modal

from z_Chip_c3_dbGet import Get_CheckChipIpAdressNotExists
from z_Chip_c3_dbGet import Get_CheckChipNumberNotExists
from z_Chip_c3_dbGet import Get_ChipIDbychipNumber

from z_Chip_c3_dbPost import Post_CreateChip

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
                InsertHistoryUser(iddochip,"Chip: "+ chip.chip_num + 
                                            " ip: " + chip.chip_ip + 
                                            " cadastrado por: " + name)
                return ResponseNewChip_Modal(chip,True,'0')
            else:
                return ResponseNewChip_Modal(chip,False,'3')
        else:
            return ResponseNewChip_Modal(chip,False,'2')
    else:
        return ResponseNewChip_Modal(chip,False,'1')
    return ResponseNewChip_Modal(chip,False,'3')


