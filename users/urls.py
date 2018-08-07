from django.conf.urls import url, include
from django.contrib import admin

#import views
from users import z_User_c1_views
from users import z_Chip_c1_views

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
    
    
    
    

    
    
]