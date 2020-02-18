from django.urls import path
from login import views
from django.contrib.auth import views as auth_views

app_name = 'login'

urlpatterns =[
    path('', views.LogginIn, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.CreateUser, name='register'),
    ]