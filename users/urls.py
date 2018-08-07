from django.conf.urls import url, include
from django.contrib import admin

#import views
from users import z1_views_User

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    url( r'DeleteUsers'         , z1_views_User.DeleteUser_View                 ),
    url( r'EditUser'            , z1_views_User.EditUserType_View               ),
    url( r'HistoryUsers'        , z1_views_User.GetHystoryUser_View             ),
    url( r'ListDesactiveUsers'  , z1_views_User.DesactivateListUsers_View       ),
    url( r'ListUsers'           , z1_views_User.ListUsers_View                  ),
    url( r'newUser'             , z1_views_User.NewUser_View                    ),
    url( r'login'               , z1_views_User.Userlogin_View                  ),
    url( r'ReactiveUsers'       , z1_views_User.ReactivateUser_View             ),
    url( r'ResetPasswordUsers'  , z1_views_User.ResetPasswordStandart_View      ),
    url( r'newPassword'         , z1_views_User.NewPassword_View      ),
    # url( r'newUser',       z1_views_User.NewUser       ),
    
    
    
    # url( r'HistoryUsers',  z1_views_User.historyUsers  ),
    

    
    #url(r'newChip',views.newChip)
    
]