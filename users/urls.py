from django.conf.urls import url, include
from django.contrib import admin

import views

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    url(r'/login',views.Userlogin),

    url(r'/newUser',views.NewUser),
    url(r'/ListUsers',views.ListUsers),
    url(r'/HistoryUsers',views.historyUsers),

    url(r'/newChip',views.newChip)
    
]