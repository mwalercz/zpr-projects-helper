from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Lecturer(models.Model):
    user = models.OneToOneField('common.CustomUser', primary_key=True)