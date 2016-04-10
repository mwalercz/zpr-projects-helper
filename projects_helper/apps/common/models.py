from django.contrib.auth.models import User, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    type_choices = (
        ('S', 'Student'),
        ('L', 'Lecturer'),
    )
    user_type = models.CharField(max_length=2,
                                 choices=type_choices,
                                 default='S')
