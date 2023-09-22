from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Admin(AbstractUser):
    """ 
    Administrator, inherits from AbstractUser.
    """
    username = models.CharField(max_length=40, unique=True)
    correo = models.CharField(max_length=40, unique=True)
    firstname = models.TextField()
    lastname = models.TextField()
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "correo"

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"
    class Meta:
        app_label = 'app1'

class Emprendedor(models.Model):
    """ 
    Emprendedor 
    """
    username = models.CharField(max_length=40, unique=True, primary_key=True)
    correo = models.CharField(max_length=40, unique=True)
    firstname = models.TextField()
    lastname = models.TextField()
    degree = models.TextField()
    institution = models.TextField()
    gender = models.TextField()
    age = models.IntegerField()
    country = models.TextField()
    studyField = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"
    class Meta:
        app_label = 'app1'

