from django.conf.urls import url, include
from django.contrib import admin

#import views
import z1_views_User

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    url(r'login',z1_views_User.Userlogin_View),

    # url( r'newUser',       z1_views_User.NewUser       ),
    url( r'ListUsers',     z1_views_User.ListUsers     ),
    # url( r'HistoryUsers',  z1_views_User.historyUsers  ),
    # url( r'DeleteUsers',   z1_views_User.DeleteUser    ),

    #url(r'newChip',views.newChip)
    
]