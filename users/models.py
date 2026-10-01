from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import SAUDI_PHONE_VALIDATOR

class User(AbstractUser):
    
    class Role(models.TextChoices):
        MEMBER = 'member', 'Member'
        LIBRARIAN = 'librarian', 'Librarian'
        MANAGER = 'manager', 'Manager'
        
    role = models.CharField(
        max_length=10, # Longest role is 9 characters, +1 for margin
        choices=Role.choices,
        default=Role.MEMBER,
    )
    
    phone = models.CharField(
        max_length=10,
        blank=False,
        validators=[SAUDI_PHONE_VALIDATOR],
        unique=True,
    )
    
    email = models.EmailField(
        unique=True,
    )
    
    first_name = models.CharField(
        max_length=15,  
    )
    last_name = models.CharField(
        max_length=15,
    )
    

    REQUIRED_FIELDS = ['email', 'phone', 'first_name', 'last_name'] 


