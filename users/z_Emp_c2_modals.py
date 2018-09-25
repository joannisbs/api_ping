from rest_framework import serializers


class Empresa_Serializer ( serializers.Serializer ):
    emp_nome        = serializers.CharField      ( max_length = 12 )
    empdata_cnpj    = serializers.CharField      ( max_length = 18 )
    empdata_email   = serializers.CharField      ( max_length = 60 )
    empdata_razao   = serializers.CharField      ( max_length = 90 )
    empdata_resp    = serializers.CharField      ( max_length = 45 )
    empdata_tel     = serializers.CharField      ( max_length = 14 )

    end_bairro      = serializers.CharField      ( max_length = 45 )
    end_cep         = serializers.CharField      ( max_length = 45 )
    end_cidade      = serializers.CharField      ( max_length = 45 )
    end_comp        = serializers.CharField      ( max_length = 45 )
    end_num         = serializers.CharField      ( max_length = 45 )
    end_ref         = serializers.CharField      ( max_length = 45 )
    end_rua         = serializers.CharField      ( max_length = 60 )
    end_uf          = serializers.CharField      ( max_length = 2  )

    cont_On         = serializers.CharField      ( max_length = 3  )   
    cont_Tot        = serializers.CharField      ( max_length = 3  )   
    emp_ativo       = serializers.BooleanField   ( default =  True )  