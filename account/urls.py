from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # rejestracja
    path('login/', auth_views.LoginView.as_view(), name='login'),  # login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # logout
]
