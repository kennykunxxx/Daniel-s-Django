from django.urls import path
from dvd import views

app_name = 'dvd'

urlpatterns = [
    path('add/<int:movie_id>', views.add_movie_cart, name='add_movie'),
    path('remove/<int:movie_id>', views.remove_movie_cart, name='remove_movie'),
    path('', views.cart_detail, name='cart_detail'),
    ]
