from users.models import Empresas, HistoryEmpresas
from django.db.models import Q
from z_User_c0_obj import Get_ListSizeRspObject

from z_Emp_c0_obj import Emp_Object , HistoryGenericObject

def Get_CheckIfEmpNameNotExists(name):
    try:
        empresas =  Empresas.objects.filter(emp_nome = name)
        # Existe Apenas um usuario com este nome no banco. 
        for empresa in empresas:
            empresa.number = '=)'
            return True
        return False
    except:
        return False

def Get_EmprById ( ids ):
    try:
        empresas =  Empresas.objects.filter(id = ids)
        # Existe Apenas um usuario com este nome no banco. 
        for empresa in empresas:
            return empresa.emp_nome
        return False
    except:
        return False
         
def Get_EmpListSize ( pagina, search, ativo ):
    fimPaginacao  = int(pagina) * 20
    initPaginacao = fimPaginacao - 20

    if search == 'all':
        sizeofListofEmps = len( Empresas.objects.filter( emp_ativo = ativo ))
            
    else:
        sizeofListofEmps = len( Empresas.objects.filter(
            Q( emp_nome__icontains       = search , emp_ativo = ativo )|

            Q( empdata_cnpj__icontains   = search , emp_ativo = ativo )|
            Q( empdata_email__icontains  = search , emp_ativo = ativo )|
            Q( empdata_razao__icontains  = search , emp_ativo = ativo )|
            Q( empdata_resp__icontains   = search , emp_ativo = ativo )|
            Q( empdata_tel__icontains    = search , emp_ativo = ativo )|

            Q( end_bairro__icontains     = search , emp_ativo = ativo )|
            Q( end_cep__icontains        = search , emp_ativo = ativo )|
            Q( end_cidade__icontains     = search , emp_ativo = ativo )|
            Q( end_comp__icontains       = search , emp_ativo = ativo )|
            Q( end_num__icontains        = search , emp_ativo = ativo )|
            Q( end_ref__icontains        = search , emp_ativo = ativo )|
            Q( end_rua__icontains        = search , emp_ativo = ativo )|
            Q( end_uf__icontains         = search , emp_ativo = ativo )))

    toBeNext = 0

    if fimPaginacao  > sizeofListofEmps:
        fimPaginacao = sizeofListofEmps
        toBeNext     = 1

    response         = Get_ListSizeRspObject()
    response.initpag = initPaginacao
    response.endpag  = fimPaginacao
    response.size    = sizeofListofEmps
    response.next    = toBeNext
    
    
    return response


def Get_ListofEmpss ( pagina, search, ativo ):

    ToBeSearch = False

    response = []
    
    fimPaginacao  = int(pagina) * 13
    initPaginacao = fimPaginacao - 13

    if search == 'all':
        sizeofListofEmps = ( Empresas.objects.filter( emp_ativo = ativo )
                              .order_by("emp_nome")[initPaginacao:fimPaginacao])
            
    else:
        sizeofListofEmps = ( Empresas.objects.filter(
            Q( emp_nome__icontains       = search , emp_ativo = ativo )|

            Q( empdata_cnpj__icontains   = search , emp_ativo = ativo )|
            Q( empdata_email__icontains  = search , emp_ativo = ativo )|
            Q( empdata_razao__icontains  = search , emp_ativo = ativo )|
            Q( empdata_resp__icontains   = search , emp_ativo = ativo )|
            Q( empdata_tel__icontains    = search , emp_ativo = ativo )|

            Q( end_bairro__icontains     = search , emp_ativo = ativo )|
            Q( end_cep__icontains        = search , emp_ativo = ativo )|
            Q( end_cidade__icontains     = search , emp_ativo = ativo )|
            Q( end_comp__icontains       = search , emp_ativo = ativo )|
            Q( end_num__icontains        = search , emp_ativo = ativo )|
            Q( end_ref__icontains        = search , emp_ativo = ativo )|
            Q( end_rua__icontains        = search , emp_ativo = ativo )|
            Q( end_uf__icontains         = search , emp_ativo = ativo ))
                              .order_by("emp_nome")[initPaginacao:fimPaginacao])

    for item in sizeofListofEmps:
        ToBeSearch = True
        empresa   = Emp_Object()
        empresa   = item
        # empresa.empdata_cnpj    = esa.empdata_cnpj
        # empresa.empdata_email   = esa.empdata_email
        # empresa.empdata_razao   = esa.empdata_razao
        # empresa.empdata_resp    = esa.empdata_resp
        # empresa.empdata_tel     = esa.empdata_tel
        # empresa
        # empresa
        # empresa
        

        response.append(empresa)

    if ToBeSearch:
        return response
    return False

def Get_EmpHistoryListSize ( pagina, search, empres ):
    fimPaginacao  = int(pagina) * 13
    initPaginacao = fimPaginacao - 13

    if search == 'all':
        sizeofListofEmps = len( HistoryEmpresas.objects.filter(
             ids = empres  ))
            
    else:
        sizeofListofEmps = len( HistoryEmpresas.objects.filter(
            Q( hora__icontains       = search  , ids = empres )|

            Q( event__icontains   = search , ids = empres )))

    toBeNext = 0

    if fimPaginacao  > sizeofListofEmps:
        fimPaginacao = sizeofListofEmps
        toBeNext     = 1

    response         = Get_ListSizeRspObject()
    response.initpag = initPaginacao
    response.endpag  = fimPaginacao
    response.size    = sizeofListofEmps
    response.next    = toBeNext
    
    
    return response


def Get_HistoryListofEmpss ( pagina, search, empres ):

    ToBeSearch = False

    response = []
    
    fimPaginacao  = int(pagina) * 20
    initPaginacao = fimPaginacao - 20

    if search == 'all':
        sizeofListofEmps = ( HistoryEmpresas.objects.filter( ids = empres  )
                              .order_by("-id")[initPaginacao:fimPaginacao])
            
    else:
        sizeofListofEmps = ( HistoryEmpresas.objects.filter(            
            
            Q( hora__icontains       = search , ids = empres  )|

            Q( event__icontains   = search , ids = empres ))
            .order_by("-id")[initPaginacao:fimPaginacao])

    for item in sizeofListofEmps:
        ToBeSearch = True
        empresa   = HistoryGenericObject()
        empresa   = item
       

        response.append(empresa)

    if ToBeSearch:
        return response
    return False