from users.models import Chip

def Updt_DeleteChip(ids):
    try:
        chips =  Chip.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for chi in chips:
    
            chi.chip_ativo = 'n'
            chi.save()
        return True
    except:
        return False

def Updt_ActiveChip(ids):
    try:
        chips =  Chip.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for chi in chips:
    
            chi.chip_ativo = 's'
            chi.save()
        return True
    except:
        return False

def Updt_EditIpChip(chipid,chipip,chipoper):
    try:
        chips =  Chip.objects.filter(id = chipid)

        # Existe Apenas um usuario com este nome no banco. 
        for chi in chips:
    
            chi.chip_ip = chipip
            chi.chip_oper = chipoper
            chi.save()
        return True
    except:
        return False
