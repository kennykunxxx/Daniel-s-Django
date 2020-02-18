from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.DateField()
    rating = models.FloatField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    
    def __str__(self):
        return self.title