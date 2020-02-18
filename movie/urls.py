from django.urls import path
from movie import views

app_name = 'movie'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name = 'search'),
    path('detail/<int:search_id>/', views.detail, name = 'detail'),
    #path('add/<str:search_id>/<str:search_overview>/<str:search_release_date>/', views.add, name = 'add'),
    path('add/<int:search_id>', views.add, name = 'add'),
    path('user_list/', views.user_list, name='user_list'),
    path('delete/<int:movie_id>/', views.delete_movie, name = 'delete_movie')
    ] 
    
    