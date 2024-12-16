from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    HOUSE_CHOICES = [
        ('Gryffindor', 'Gryffindor'),
        ('Slytherin', 'Slytherin'),
        ('Ravenclaw', 'Ravenclaw'),
        ('Hufflepuff', 'Hufflepuff'),
    ]
    house = models.CharField(max_length=50, choices=HOUSE_CHOICES, verbose_name="Casa de Hogwarts")

    def __str__(self):
        return f"{self.user.username} - {self.house}"
