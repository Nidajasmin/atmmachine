

from django.urls import path
from . import views

urlpatterns = [
    # Dashboard 
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_user, name='register_user'),
    path('users/', views.user_list, name='user_list'),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),

   #(Insert Card Page)
    path('payment/', views.insert_card, name='payment'),  

    # ATM Operations
    path('atm/menu/', views.atm_menu, name='atm_menu'),
    path('atm/balance/', views.check_balance, name='check_balance'),
    path('atm/deposit/', views.deposit, name='deposit'),
    path('atm/withdraw/', views.withdraw, name='withdraw'),
    path('atm/thankyou/', views.thank_you, name='thank_you'),
]













# # from django.urls import path
# # from .views import register_user
# # from api import views

# # urlpatterns = [
# #     path('', views.dashboard, name='dashboard'),   
# #     path('register/', register_user, name='register_user'),
# #     path('users/', views.user_list, name='user_list'),  

# #     path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
# #     path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
# #     path('payment/', views.insert_card, name='welcome'), 
# #     path('atm/menu/', views.atm_menu, name='atm_menu'),   
# #     path('atm/balance/', views.check_balance, name='check_balance'),
# #     path('atm/deposit/', views.deposit, name='deposit'),
# #     path('atm/withdraw/', views.withdraw, name='withdraw'),
# #     path('atm/thankyou/', views.thank_you, name='thank_you'),

# # ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     # Dashboard & User Management
#     path('', views.dashboard, name='dashboard'),
#     path('register/', views.register_user, name='register_user'),
#     path('users/', views.user_list, name='user_list'),
#     path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
#     path('delete/<int:user_id>/', views.delete_user, name='delete_user'),

#     # ATM Entry & Authentication
#     path('payment/', views.payment, name='payment'), 
#      # Changed from insert_card to payment
#     path('insert_card/', views.insert_card, name='insert_card'), 


#     # ATM Operations
#     path('atm/menu/', views.atm_menu, name='atm_menu'),
#     path('atm/balance/', views.check_balance, name='check_balance'),
#     path('atm/deposit/', views.deposit, name='deposit'),
#     path('atm/withdraw/', views.withdraw, name='withdraw'),
#     path('atm/thankyou/', views.thank_you, name='thank_you'),
# ]
