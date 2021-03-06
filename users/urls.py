from django.conf.urls import url, include
from django.contrib import admin

#import views
from users import z_User_c1_views
from users import z_Chip_c1_views
from users import z_Emp_c1_views

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    url( r'DeleteUsers'         , z_User_c1_views.DeleteUser_View               ),
    url( r'EditUser'            , z_User_c1_views.EditUserType_View             ),
    url( r'HistoryUsers'        , z_User_c1_views.GetHystoryUser_View           ),
    url( r'ListDesactiveUsers'  , z_User_c1_views.DesactivateListUsers_View     ),
    url( r'ListUsers'           , z_User_c1_views.ListUsers_View                ),
    url( r'newUser'             , z_User_c1_views.NewUser_View                  ),
    url( r'login'               , z_User_c1_views.Userlogin_View                ),
    url( r'ReactiveUsers'       , z_User_c1_views.ReactivateUser_View           ),
    url( r'ResetPasswordUsers'  , z_User_c1_views.ResetPasswordStandart_View    ),
    url( r'newPassword'         , z_User_c1_views.NewPassword_View              ),
    

    url(r'newChip'              ,z_Chip_c1_views.NewChip_View                   ),
    url(r'listDesactivedChip'   ,z_Chip_c1_views.listDesactivedChip_View        ) ,
    url(r'listChip'             ,z_Chip_c1_views.ListChip_View                  ),
    url(r'ChipDelete'           ,z_Chip_c1_views.ChipDelete_View                ),
    url(r'ChipActive'           ,z_Chip_c1_views.ChipActive_View                ),
    url(r'ChipEditIp'           ,z_Chip_c1_views.EditIpChip_View                ),
    url(r'ChipListHistory'      ,z_Chip_c1_views.GetHystoryChip_View            ),
    
    
    
    url(r'NewCompany'           ,z_Emp_c1_views.NewEmp_View                     ),
    url(r'EditCompany'          ,z_Emp_c1_views.EditEmp_View                    ),
    url(r'ListDesactivedCompany',z_Emp_c1_views.ListEmpDesactive_View           ),
    url(r'ListActivedCompany'   ,z_Emp_c1_views.ListEmpActive_View              ),
    url(r'ListHistoryCompany'   ,z_Emp_c1_views.ListHistoryEmp_View             ), 
    url(r'ToDesactiveCompany'   ,z_Emp_c1_views.ToDesactive_View                ),    
    url(r'ToReactiveCompany'    ,z_Emp_c1_views.ToReactive_View                 ), 
]