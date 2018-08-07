from z_Chip_c0_obj import db_ChipObject

def R_GetNewChip_Interface(data):
    response                = db_ChipObject()
    response.chip_ip        = data.get('chip_ip')
    response.chip_data      = data.get('chip_Data')
    response.chip_oper      = data.get('chip_Operadora')
    response.chip_num       = data.get('chip_Numchip')
    response.chip_ativo     = 's'
    response.chip_where     = 'e'
    response.chip_whedes    = 0
 
    return response
    
  