# enccoding: utf-8

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
from z_Emp_c3_dbGet import Get_HistoryListofEmpss
from z_Emp_c3_dbGet import Get_EmpHistoryListSize

from z_Emp_c3_dbUpdt import Updt_DeleteEmp
from z_Emp_c3_dbUpdt import Updt_ActiveEmp
from z_Emp_c3_dbUpdt import Updt_DateEmp

from z_Emp_c2_modals import Empresa_Serializer
from z_Emp_c2_modals import History_Serializer

from z__Dicts import Dict_respostas_List



def EditCompany_Method ( oldemp, newemp, iduser):
    
    
    emp                 = NewEmp_Object()

    emp.emp_nome        =  unicode(newemp.get ( 'emp_nome'      ))
    emp.empdata_cnpj    =  unicode(newemp.get ( 'empdata_cnpj'  ))
    emp.empdata_email   =  unicode(newemp.get ( 'empdata_email' ))
    emp.empdata_razao   =  unicode(newemp.get ( 'empdata_razao' ))
    emp.empdata_resp    =  unicode(newemp.get ( 'empdata_resp'  ))
    emp.empdata_tel     =  unicode(newemp.get ( 'empdata_tel'   ))

    emp.end_bairro      =  unicode(newemp.get ( 'end_bairro'    ))
    emp.end_cep         =  unicode(newemp.get ( 'end_cep'       ))
    emp.end_cidade      =  unicode(newemp.get ( 'end_cidade'    ))
    emp.end_comp        =  unicode(newemp.get ( 'end_comp'      ))
    emp.end_num         =  unicode(newemp.get ( 'end_num'       ))
    emp.end_ref         =  unicode(newemp.get ( 'end_ref'       ))
    emp.end_rua         =  unicode(newemp.get ( 'end_rua'       ))
    emp.end_uf          =  unicode(newemp.get ( 'end_uf'        ))
    
    print "sucesso"
    sucesso = Updt_DateEmp(oldemp, emp)
    print "2"
    if sucesso[0] and sucesso[1]:
        print "2"
        usuario = Get_UserById ( iduser )
        print "sucesso1"
        tamanho = len(sucesso[1])
        print "sucesso1"
        string = ( usuario + ' fez ' + str(tamanho) + u' alterações')
        print "sucesso1"
        hsucess = InsertHistoryEmp ( oldemp, unicode(string) )
        print "sucesso"
        husucess = InsertHistoryUser  ( iduser , emp.emp_nome + 'foi alterada em ' + str(tamanho) + ' campos')
        print "aqui"
        num = 1
        for item in sucesso[1]:
            print "aqui2"
            hsucess = InsertHistoryEmp    ( oldemp, u'Alteração '+ str(num) +' | Campo: ' + item[0] +" | Para:" + item[2])
            husucess = InsertHistoryUser  ( iduser, u'Alteração ' + str(num) +' | Campo: ' + item[0] +" | Para:" + item[2])
            num = num + 1

        if husucess:
            return 'sucesso'
            
        return 'falhahistory'
    return 'falha' 
    
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

def ListHistoryCompany_Method ( dado ):
    search = dado.get ( 'search' )
    pagina = dado.get ( 'pagina' )
    Empres = dado.get ( 'ObjIds' )

    response              = []
    listofEmpsSerializada = []
    listEmp               = False
    sucessoGetList        = 'inicializado'

    try: 

        sizeof = Get_EmpHistoryListSize ( pagina, search , Empres)
       
        sizeof = SizeListUser_Serializer(sizeof)
        
        sizeof = sizeof.data
        sucessoGetList = 'sucesso'

    except:
        sucessoGetList = 'erroSize'
    
    try:
        
        listEmp = Get_HistoryListofEmpss ( pagina, search , Empres )
        
        if not listEmp:
            sucessoGetList = 'listavazia'
            listEmp = []
    except:
        sucessoGetList = 'erroList'
        listEmp = []
        print "FALHA LISTY"
    
 
    for item in listEmp:
        Emp     = History_Serializer ( item )
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

        hsucess  = InsertHistoryEmp   ( empresa, u'Excluída por '    + usuario   + ' motivo: ' + motivo )
        husucess = InsertHistoryUser  ( iduser , 'Exluiu a empresa ' + name_empr + ' motivo: ' + motivo )
        
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
        print sucesso
        if sucesso:
            usuario = Get_UserById ( iduser )
            
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastrada por ' + usuario )
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Nome:   ' + unicode(emp.emp_nome      ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Cnpj:   ' + unicode(emp.empdata_cnpj  ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Email:  ' + unicode(emp.empdata_email ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Razao:  ' + unicode(emp.empdata_razao ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Resp.:  ' + unicode(emp.empdata_resp  ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Tel.:   ' + unicode(emp.empdata_tel   ))

            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Bairro: ' + unicode(emp.end_bairro    )) 
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Cep:    ' + unicode(emp.end_cep       ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Cidade: ' + unicode(emp.end_cidade    ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Comp:   ' + unicode(emp.end_comp      ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Num:    ' + unicode(emp.end_num       ))            
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Ref:    ' + unicode(emp.end_ref       ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Rua:    ' + unicode(emp.end_rua       ))
            hsucess = InsertHistoryEmp ( sucesso,u'Cadastro | Campo: Uf:     ' + unicode(emp.end_uf)       )

            
            husucess = InsertHistoryUser  ( iduser , 'Cadastrou a empresa ' + unicode(dado.get('emp_nome') ))
            
            if husucess:
                return 'sucesso'
               
            return 'falhahistory'
        return 'falha' 
    else:
        return 'ja_existe'



def InsertHistoryEmp ( Empid, hystory ):
    histo = Post_historyObject()
    time = GetTimeDB()
    histo.ids = int(Empid)
    histo.hora = time
    histo.event = unicode(hystory)
    histo = Post_History_EmpreDbSeri(histo)
    return histo.Save(histo.data)
   