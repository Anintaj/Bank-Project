from django.urls import path
from . import views
app_name='bankapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('create',views.create,name='create'),
    path('accform',views.accform,name='accform'),
    path('account_application',views.account_application,name='account_application'),
    path('logout',views.logout,name='logout'),

]