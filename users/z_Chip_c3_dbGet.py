from users.models import Chip

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