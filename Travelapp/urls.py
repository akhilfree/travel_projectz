from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('register1/',views.register1,name='register1'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='login')

]