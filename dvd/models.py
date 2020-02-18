from django.db import models
from movie.models import movie
from decimal import Decimal
from django.contrib.auth.models import User

class Order(models.Model):
    buy_choice = (('True', True), ('False', False),)
    buy = models.CharField(max_length=20, choices=buy_choice, default='False')

class Dvd(models.Model):
    movie_dvd = models.ForeignKey(movie, on_delete=models.CASCADE, related_name='dvd')
    movie_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='dvd_orders', default=None)
    owned = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    user_dvd = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dvd_form', null=True, blank=True)


    
# Create your models here.
