# -*- coding: utf-8 -*-
from users.models import Empresas
from z_Emp_c0_obj import NewEmp_Object

def Updt_DeleteEmp(ids):
    try:
        Emps =  Empresas.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for empresa in Emps:
    
            empresa.emp_ativo = False
            empresa.save()
        return True
    except:
        return False

def Updt_ActiveEmp(ids):
    try:
        Emps =  Empresas.objects.filter(id = ids)

        # Existe Apenas um usuario com este nome no banco. 
        for empresa in Emps:
    
            empresa.emp_ativo = True
            empresa.save()
        return True
    except:
        return False

def Updt_DateEmp( oldemp, newemp):
    print oldemp

    listofrespostes = []
    try:
        Emps =  Empresas.objects.filter(id = oldemp)

        # Existe Apenas um usuario com este nome no banco. 
        for empresa in Emps:
            

            if empresa.emp_nome      != newemp.emp_nome     :
                listofrespostes.append([ 'nome' ,        empresa.emp_nome , newemp.emp_nome])  

            if empresa.empdata_cnpj  != newemp.empdata_cnpj :
                listofrespostes.append([ 'cnpj',         empresa.empdata_cnpj  , newemp.empdata_cnpj ]) 

            if empresa.empdata_email != newemp.empdata_email:
                listofrespostes.append([ 'email',        empresa.empdata_email , newemp.empdata_email])  

            if empresa.empdata_razao != newemp.empdata_razao:
                listofrespostes.append([ 'razao social', empresa.empdata_razao , newemp.empdata_razao])   

            if empresa.empdata_resp  != newemp.empdata_resp :
                listofrespostes.append([ 'responsavel',  empresa.empdata_resp  , newemp.empdata_resp ]) 

            if empresa.empdata_tel   != newemp.empdata_tel  :
                listofrespostes.append([ 'telefone',     empresa.empdata_tel   , newemp.empdata_tel  ])  

            if empresa.end_bairro    != newemp.end_bairro   :
                listofrespostes.append([ 'bairro',       empresa.end_bairro    , newemp.end_bairro   ]) 

            if empresa.end_cep       != newemp.end_cep      :
                listofrespostes.append([ 'cep',          empresa.end_cep       , newemp.end_cep      ])   

            if empresa.end_cidade    != newemp.end_cidade   :
                listofrespostes.append([ 'cidade',       empresa.end_cidade    , newemp.end_cidade   ])   

            if empresa.end_comp      != newemp.end_comp     :
                listofrespostes.append([ 'complemento',  empresa.end_comp      , newemp.end_comp     ])  

            if empresa.end_num       != newemp.end_num      :
                listofrespostes.append([ 'end_numero',   empresa.end_num       , newemp.end_num      ])   

            if empresa.end_ref       != newemp.end_ref      :
                listofrespostes.append([ 'ponto de referencia', empresa.end_ref, newemp.end_ref      ])   

            if empresa.end_rua       != newemp.end_rua      :
                listofrespostes.append([ 'rua',          empresa.end_rua       , newemp.end_rua      ])  

            if empresa.end_uf        != newemp.end_uf       :
                listofrespostes.append([ 'estado',       empresa.end_uf        , newemp.end_uf       ])  


            empresa.emp_nome      = newemp.emp_nome       
            empresa.empdata_cnpj  = newemp.empdata_cnpj  
            empresa.empdata_email = newemp.empdata_email  
            empresa.empdata_razao = newemp.empdata_razao   
            empresa.empdata_resp  = newemp.empdata_resp  
            empresa.empdata_tel   = newemp.empdata_tel    

            empresa.end_bairro    = newemp.end_bairro    
            empresa.end_cep       = newemp.end_cep         
            empresa.end_cidade    = newemp.end_cidade      
            empresa.end_comp      = newemp.end_comp       
            empresa.end_num       = newemp.end_num         
            empresa.end_ref       = newemp.end_ref         
            empresa.end_rua       = newemp.end_rua        
            empresa.end_uf        = newemp.end_uf         


            empresa.save()

                   
        return [True , listofrespostes]
    except:
        return [False, 0]
