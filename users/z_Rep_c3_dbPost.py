# enccoding: utf-8
from rest_framework import serializers
from users.models import Empresas
from users.models import HistoryEmpresas


class Post_Empresas_DbSeri ( serializers.Serializer ):
    
    emp_nome        = serializers.CharField     ( max_length=12 )
    empdata_cnpj    = serializers.CharField     ( max_length=18 )
    empdata_email   = serializers.CharField     ( max_length=60 )
    empdata_razao   = serializers.CharField     ( max_length=90 )
    empdata_resp    = serializers.CharField     ( max_length=45 )
    empdata_tel     = serializers.CharField     ( max_length=14 )

    end_bairro      = serializers.CharField     ( max_length=45 )
    end_cep         = serializers.CharField     ( max_length=45 )
    end_cidade      = serializers.CharField     ( max_length=45 )
    end_comp        = serializers.CharField     ( max_length=45 )
    end_num         = serializers.CharField     ( max_length=45 )
    end_ref         = serializers.CharField     ( max_length=45 )
    end_rua         = serializers.CharField     ( max_length=60 )
    end_uf          = serializers.CharField     ( max_length=2  )

    cont_On         = serializers.CharField     ( max_length=3  )
    cont_Tot        = serializers.CharField     ( max_length=3  )

    def Save ( self, data ):
        
        emp = Empresas.objects.create ( **data )
        return emp.id

       

class Post_History_EmpreDbSeri ( serializers.Serializer ):
    ids             = serializers.IntegerField  ( default=0     )
    hora            = serializers.CharField     ( max_length=17 )
    event           = serializers.CharField     ( max_length=100)

    def Save ( self, data ):
        try:
            HistoryEmpresas.objects.create ( **data)
            return True

        except:
            return False