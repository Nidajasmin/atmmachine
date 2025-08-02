from django.urls import path
from .views import register_user
from api import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),   
    path('register/', register_user, name='register_user'),
    path('users/', views.user_list, name='user_list'),  
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('atm/', views.atm_interface, name='atm_interface')
]
