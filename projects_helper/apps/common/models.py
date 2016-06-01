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

    @property
    def is_full(self):
        if len(self.student_set.all()) == 2:
            return True
        else:
            return False

    @staticmethod
    def remove_empty():
        for team in Team.objects.all():
            if len(team.students_in_team()) == 0:
                team.delete()

    def __str__(self):
        tmp_str = ""
        for student in self.student_set.all():
            tmp_str += student.user.username + " "

        if tmp_str == "":
            return "Team " + str(self.pk)
        else:
            return tmp_str


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    lecturer = models.ForeignKey('common.Lecturer',
                                 on_delete=models.CASCADE)
    team_assigned = models.OneToOneField('common.Team',
                                         null=True,

                                         blank=True)

    def teams_with_preference(self):
        return Team.objects.filter(project_preference = self)

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
