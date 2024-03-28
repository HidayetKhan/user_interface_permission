from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission

# Create your models here.

class USerMaster(models.Model):
     CHOICES = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('FullStack', 'FullStack'),
    )
     name=models.CharField(max_length=200)
     email=models.EmailField()
     phone=models.CharField(max_length=10)
     date_of_birth=models.DateTimeField()
     city=models.CharField(max_length=100)
     my_field = models.CharField(max_length=50, choices=CHOICES)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now_add=True)
     is_active=models.BooleanField(default=True)
      

     def __str__(self):
        return self.name
     
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('super', 'super'),
        ('user', 'user'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    # Add related_name to groups field
    groups = models.ManyToManyField(Group, related_name='custom_users')

    # Add related_name to user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_users_permissions',
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )

class User(models.Model):
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=100)

    
