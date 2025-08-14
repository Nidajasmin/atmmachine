from django.urls import path,include
from . import views
from .views import AdminLoginView, BankUserListView, BankUserDetailView








urlpatterns = [
    # Dashboard 
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_user, name='register_user'),
    path('users/', views.user_list, name='user_list'),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),

    # (Insert Card Page)
    path('payment/', views.insert_card, name='payment'),  

    # ATM Operations
    path('atm/menu/', views.atm_menu, name='atm_menu'),
    path('atm/balance/', views.check_balance, name='check_balance'),
    path('atm/deposit/', views.deposit, name='deposit'),
    path('atm/withdraw/', views.withdraw, name='withdraw'),
    path('atm/transaction/', views.transaction, name='transaction'),
    path('atm/thankyou/', views.thank_you, name='thank_you'),
     path("api/admin/login/", AdminLoginView.as_view(), name="admin-login"),
    path("api/admin/users/", BankUserListView.as_view(), name="user-list"),
    path("api/admin/users/<int:pk>/", BankUserDetailView.as_view(), name="user-detail"),
    
]
