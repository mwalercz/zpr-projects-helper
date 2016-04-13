from enum import Enum

from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Team(models.Model):
    project_preference = models.ForeignKey('common.Project',
                                           null=True,
                                           blank=True)

        # def students_number(self):
        #     students_in_team = Student.objects.get(team_id=self.pk)
        #     return len(students_in_team)

        # def save(self, *args, **kwargs):
        #     # team is being created for the first time == no pk
        #     if self.pk is None:
        #         return super(Team, self).save(*args, **kwargs)
        #
        #     # proceed according to students_number
        #     else:
        #         students_number = self.students_number()
        #         if students_number == 0:
        #             self.delete()
        #         elif students_number > 2:
        #             raise TooManyStudentsInTeam
        #         else:
        #             return super(Team, self).save(*args, **kwargs)


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
        ('S', 'Student'),
        ('L', 'Lecturer'),
    )
    user_type = models.CharField(max_length=2,
                                 choices=type_choices,
                                 default='S')


class Student(models.Model):
    user = models.OneToOneField(CustomUser,
                                primary_key=True)
    team = models.ForeignKey('common.Team',
                             blank=True)

    def save(self, *args, **kwargs):
        if self.team_id is None:
            self.team = Team.objects.create()
        return super(Student, self).save(*args, **kwargs)


class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser,
                                primary_key=True)

