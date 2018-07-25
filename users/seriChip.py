from rest_framework        import serializers
from users.models          import Chip
from respostas             import Resposta_padrao_array
from users.seriUserHistory import CriaHistorico
from users.seriUser        import GetUserById
from users.seriHistoryChip import AdcionaHistoryChip

class ChipSerializer(serializers.Serializer):
    id            = serializers.IntegerField(read_only=True)
    chip_ip       = serializers.CharField(max_length=45)
    chip_num      = serializers.CharField(max_length=8)
    chip_oper     = serializers.CharField(max_length=15)
    chip_data     = serializers.CharField(max_length=17)
    chip_where    = serializers.CharField(max_length=1, default='0')
    chip_whedes   = serializers.IntegerField(default=0)

    def cria(self,data):
        Chip.objects.create(**data)

def createChip(data, ids):
        # Respostas Susses?, motive
        # 1 Chip Existente
        # 2 Conflito de Ip
        # 3 dados Inconsistentes

        chip_ip       = data.get('chip_ip')
        chip_num      = data.get('chip_Numchip')
        chip_oper     = data.get('chip_Operadora')
        chip_data     = data.get('chip_Data')
        chip_where    = '0'
        chip_whedes   =  0

        if len(chip_num) != 8:
            return [False,3,chip_num]
        
        if chip_ip[0:5] != '10.26':         
            if chip_ip[0:5] != '10.50':              
                if chip_ip[0:6] != '10.115':              
                    if chip_ip[0:6] != '172.40':             
                        if chip_ip[0:4] != 'host':
                            return [False,3,chip_num]

        if CheckChipNumber(chip_num):
            return [False,1,chip_num]

        if CheckChipIp(chip_ip):
            return [False,2,chip_num]


        chipObj =   ChipObj(chip_ip,chip_num,chip_oper,chip_data,chip_where,chip_whedes)
        
        if salvaChip(chipObj):
            id_chip = retornID(chip_num)
            nome = GetUserById(int(ids))
            AdcionaHistoryChip(id_chip,'O Chip foi cadastrado por: '+ 
                    str(nome)+", Num: "+ chip_num +", Ip: "+ chip_ip )
            string = ("Cadastrou o chip: " + str(chip_num) + 
                    " Ip: " + str(chip_ip) + " Opr: " + str(chip_oper))
            CriaHistorico(str(ids),string)
            return [True,0,chip_num]

def retornID(number):
    res = Chip.objects.filter(chip_num = number)
    for re in res:
        return re.id

def CheckChipIp(ip):
    if ip == 'host':
        return False
    res = Chip.objects.filter(chip_ip = ip)
    if len(res)>0:
        return True
    else:
        return False

def CheckChipNumber(number):
    res = Chip.objects.filter(chip_num = number)
    if len(res)>0:
        return True
    else:
        return False

def salvaChip(data):
    istance = ChipSerializer(data)
    istance.cria(istance.data)
    return True
    

class ChipObj:
    def __init__(self,ip,num,oper,data,where,whedes):
        self.chip_ip       = ip
        self.chip_num      = num
        self.chip_oper     = oper
        self.chip_data     = data
        self.chip_where    = where
        self.chip_whedes   = whedes