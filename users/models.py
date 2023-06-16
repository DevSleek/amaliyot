from django.db import models

# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=22)
    email = models.EmailField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
