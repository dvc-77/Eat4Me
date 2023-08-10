from django.urls import path
from django.contrib.auth import views as auth_view
from api import views

urlpatterns = [
    path('signup/', views.restaurant_sign_up, name='restaurant_sign_up'),
    path('login/', auth_view.LoginView.as_view(
        template_name='sign_in.html'), name='login'), 
    path('dashboard/', views.restaurant_dashboard, name='restaurant_dashboard'), 
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),
    path('reset/', views.password_reset, name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
]