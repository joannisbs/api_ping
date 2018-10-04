# import methodos dos usuarios
from z_User_c3_dbGet import Get_UserById
from z_User_c2_methods import InsertHistoryUser
from z_User_c2_methods import GetTimeDB
from z_User_c2_modals import SizeListUser_Serializer, ListHistoryUsers_Serializer

from z__functionsgenericas import ArrumaData 
from z__functionsgenericas import Post_historyObject
from z_User_c2_modals import S_StandardResponse_Modal 

from z_Emp_c0_obj import NewEmp_Object

from z_Emp_c3_dbPost import Post_Empresas_DbSeri
from z_Emp_c3_dbPost import Post_History_EmpreDbSeri

from z_Emp_c3_dbGet import Get_CheckIfEmpNameNotExists
from z_Emp_c3_dbGet import Get_EmpListSize
from z_Emp_c3_dbGet import Get_ListofEmpss 
from z_Emp_c3_dbGet import Get_EmprById 

from z_Emp_c3_dbUpdt import Updt_DeleteEmp
from z_Emp_c3_dbUpdt import Updt_ActiveEmp

from z_Emp_c2_modals import Empresa_Serializer

from z__Dicts import Dict_respostas_List


def ListCompany_Method ( dado, ativo ):
    search = dado.get ( 'search' )
    pagina = dado.get ( 'pagina' )

    response              = []
    listofEmpsSerializada = []
    listEmp               = False
    sucessoGetList        = 'inicializado'

    try: 
        sizeof = Get_EmpListSize ( pagina, search, ativo )
        sizeof = SizeListUser_Serializer(sizeof)
        sizeof = sizeof.data
        sucessoGetList = 'sucesso'

    except:
        sucessoGetList = 'erroSize'
    
    try:
        listEmp = Get_ListofEmpss ( pagina, search, ativo )
        if not listEmp:
            sucessoGetList = 'listavazia'
            listEmp = []
    except:
        sucessoGetList = 'erroList'
        listEmp = []
        print "FALHA LISTY"
    
 
    for item in listEmp:
        Emp     = Empresa_Serializer ( item )
        listofEmpsSerializada.append ( Emp.data )

    response.append ( Dict_respostas_List [ sucessoGetList ] )
    response.append ( sizeof )
    response.append ( listofEmpsSerializada )   
    
    return response

def DeleteCompany_Method ( dado, iduser ):
    empresa             =  dado.get ( 'id')
    motivo              =  dado.get ( 'motivo')
    
    sucess = Updt_DeleteEmp ( empresa )

    if sucess:
        
        usuario    = Get_UserById ( iduser  )
        name_empr  = Get_EmprById ( empresa )

        if not name_empr:
            return 'falha'

        print usuario
        print name_empr

        hsucess  = InsertHistoryEmp   ( empresa, 'Excluida por '     + usuario   + ' ' + motivo )
        husucess = InsertHistoryUser  ( iduser , 'Exluiu a empresa ' + name_empr + ' ' + motivo )
        
        if hsucess and husucess:      
            return 'sucesso'
        
                
        return 'falhahistory'
    return 'falha'

def ActiveCompany_Method ( dado, iduser ):
    empresa             =  dado.get ( 'id')
    motivo              =  dado.get ( 'motivo')
    
    sucess = Updt_ActiveEmp ( empresa )

    if sucess:
        
        usuario    = Get_UserById ( iduser  )
        name_empr  = Get_EmprById ( empresa )

        if not name_empr:
            return 'falha'

        print usuario
        print name_empr

        hsucess  = InsertHistoryEmp   ( empresa, 'Reativada por '      + usuario   + ' ' + motivo )
        husucess = InsertHistoryUser  ( iduser , 'Reativou a empresa ' + name_empr + ' ' + motivo )
        
        if hsucess and husucess:      
            return 'sucesso'
        
                
        return 'falhahistory'
    return 'falha'


def NewCompany_Method(dado,iduser):
    emp                 = NewEmp_Object()

    emp.emp_nome        =  dado.get ( 'emp_nome'      )
    emp.empdata_cnpj    =  dado.get ( 'empdata_cnpj'  )
    emp.empdata_email   =  dado.get ( 'empdata_email' )
    emp.empdata_razao   =  dado.get ( 'empdata_razao' )
    emp.empdata_resp    =  dado.get ( 'empdata_resp'  )
    emp.empdata_tel     =  dado.get ( 'empdata_tel'   )

    emp.end_bairro      =  dado.get ( 'end_bairro'    )
    emp.end_cep         =  dado.get ( 'end_cep'       )
    emp.end_cidade      =  dado.get ( 'end_cidade'    )
    emp.end_comp        =  dado.get ( 'end_comp'      )
    emp.end_num         =  dado.get ( 'end_num'       )
    emp.end_ref         =  dado.get ( 'end_ref'       )
    emp.end_rua         =  dado.get ( 'end_rua'       )
    emp.end_uf          =  dado.get ( 'end_uf'        )
    
    exist = Get_CheckIfEmpNameNotExists( dado.get ( 'emp_nome' ) )

    if not exist:
        empresa = Post_Empresas_DbSeri(emp)
        sucesso = empresa.Save(empresa.data)

        if sucesso:
            usuario = Get_UserById ( iduser )
            hsucess = InsertHistoryEmp ( sucesso,'Cadastrada por ' + usuario )

            if hsucess:
                husucess = InsertHistoryUser  ( iduser , 'Cadastrou a empresa ' + dado.get('emp_nome') )
                if husucess:
                    return 'sucesso'
                return 'falhahistoryUsr'
            return 'falhahistory'
        return 'falha' 
    else:
        return 'ja_existe'



def InsertHistoryEmp ( Empid, hystory ):
    histo = Post_historyObject()
    time = GetTimeDB()
    histo.ids = int(Empid)
    histo.hora = time
    histo.event = hystory
    histo = Post_History_EmpreDbSeri(histo)
    return histo.Save(histo.data)
   