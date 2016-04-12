from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from projects_helper.apps.teams.models import Team


class Student(models.Model):
    user = models.OneToOneField('common.CustomUser',
                                primary_key=True)
    team = models.ForeignKey('teams.Team')

    def save(self, *args, **kwargs):
        if self.team_id is None:
            self.team = Team.objects.create()
        return super(Student, self).save(*args, **kwargs)


