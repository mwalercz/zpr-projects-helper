from enum import Enum

from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Team(models.Model):
    project_preference = models.ForeignKey('common.Project',
                                           null=True,
                                           blank=True)

    def project_assigned(self):
        try:
            project = Project.objects.get(team_assigned=self)
            return project
        except models.ObjectDoesNotExist:
            return None


    def students_in_team(self):
        return self.student_set.all()

    def __str__(self):
        str = ""
        for student in self.student_set.all():
            str += student.user.username + " "

        if str == "":
            return "None"
        else:
            return str


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    lecturer = models.ForeignKey('common.Lecturer',
                                 on_delete=models.CASCADE)
    team_assigned = models.OneToOneField('common.Team',
                                         null=True,
                                         blank=True)

    def status(self):
        if self.team_assigned is None:
            return "free"
        else:
            return "occupied"

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    type_choices = (
        ('SU', 'SuperUser'),
        ('S', 'Student'),
        ('L', 'Lecturer'),
    )
    user_type = models.CharField(max_length=2,
                                 choices=type_choices,
                                 default='SU')


class Student(models.Model):
    user = models.OneToOneField(CustomUser,
                                primary_key=True)
    team = models.ForeignKey('common.Team',
                             blank=True)

    def save(self, *args, **kwargs):
        if self.team_id is None:
            self.team = Team.objects.create()
        return super(Student, self).save(*args, **kwargs)

    # def project_assigned(self):
    #     return self.team.project_assigned()
    #
    # def project_preference(self):
    #     return self.team.project_preference

    def __str__(self):
        return self.user.username


class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser,
                                primary_key=True)

    def __str__(self):
        return self.user.username
