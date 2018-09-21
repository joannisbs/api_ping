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


def NewCompany_Method(dado,iduser):
    emp                 = NewEmp_Object()

    emp.emp_nome        = dado.get ( 'emp_nome'      )
    emp.empdata_cnpj    = dado.get ( 'empdata_cnpj'  )
    emp.empdata_email   = dado.get ( 'empdata_email' )
    emp.empdata_razao   = dado.get ( 'empdata_razao' )
    emp.empdata_resp    = dado.get ( 'empdata_resp'  )
    emp.empdata_tel     = dado.get ( 'empdata_tel'   )

    emp.end_bairro      = dado.get ( 'end_bairro'    )
    emp.end_cep         = dado.get ( 'end_cep'       )
    emp.end_cidade      = dado.get ( 'end_cidade'    )
    emp.end_comp        = dado.get ( 'end_comp'      )
    emp.end_num         = dado.get ( 'end_num'       )
    emp.end_ref         = dado.get ( 'end_ref'       )
    emp.end_rua         = dado.get ( 'end_rua'       )
    emp.end_uf          = dado.get ( 'end_uf'        )
    
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


def InsertHistoryEmp(Empid,hystory):
    histo = Post_historyObject()
    time = GetTimeDB()
    histo.ids = int(Empid)
    histo.hora = time
    histo.event = hystory
    histo = Post_History_EmpreDbSeri(histo)
    return histo.Save(histo.data)
   