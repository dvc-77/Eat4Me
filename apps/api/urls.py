from django.urls import path
from django.contrib.auth import views as auth_view
from api import views

urlpatterns = [
    # Web Auth View
    path('signup/', views.restaurant_sign_up, name='restaurant_sign_up'),
    path('login/', auth_view.LoginView.as_view(template_name='sign_in.html'), name='login'), 
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),

    # Web View - Restaurant
    path('dashboard/', views.restaurant_dashboard, name='restaurant_dashboard'), 
    path('restaurant/meal/', views.restaurant_meal, name='restaurant_meal'),
    path('restaurant/order/', views.restaurant_order, name='restaurant_order'),
    path('restaurant/report/', views.restaurant_report, name='restaurant_report'),
    path('restaurant/account/', views.restaurant_account, name='restaurant_account'),
]