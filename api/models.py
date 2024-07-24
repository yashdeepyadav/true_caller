from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .dal import UserManager

# Create your models here.

class BaseModel(models.Model):
    """
    Base abstract timestamp model to be inherited by all models
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class User(AbstractBaseUser, BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']
    
    objects = UserManager()

    def __str__(self):
        return self.phone
    
class Contact(BaseModel):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.phone
    
class Spam(BaseModel):
    phone = models.CharField(max_length=15, unique=True)
    reported_by = models.ManyToManyField(User, related_name='spam_numbers')
    
    def __str__(self):
        return self.phone