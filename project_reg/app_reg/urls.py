from django.urls import path
from app_reg import views

app_name = 'app_reg'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('data/', views.data, name='data'),
]
