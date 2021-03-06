from django.urls import path, include
from django.contrib.auth import views as auth_views
from account import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # change password, reset password
    path('', include('django.contrib.auth.urls')),


]
