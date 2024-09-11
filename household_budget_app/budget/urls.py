from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # サインアップURL
    path('login/', auth_views.LoginView.as_view(template_name='budget/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add/', views.add_expense, name='add_expense'),
    path('list/', views.expense_list, name='expense_list'),
    path('edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    
    # Djangoの標準の認証URLを追加
    path('accounts/', include('django.contrib.auth.urls')),  # これで/accounts/login/などが使用可能になります
]


