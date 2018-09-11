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