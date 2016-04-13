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


class Student(models.Model):
    user = models.OneToOneField(CustomUser,
                                primary_key=True)
    team = models.ForeignKey('common.Team')

    def save(self, *args, **kwargs):
        if self.team_id is None:
            self.team = Team.objects.create()
        return super(Student, self).save(*args, **kwargs)


class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser,
                                primary_key=True)


class Team(models.Model):
    project_preference = models.ForeignKey('common.Project',
                                           null=True)

    def __str__(self):
        return self.name

        # def get_absolute_url(self):
        #     return reverse('teams:detail', args=[str(self.id)])

        # def save(self, *args, **kwargs):
        # if self.team_id is None:
        #         self.team = Team.objects.create()
        # return super(Student, self).save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    lecturer = models.ForeignKey(Lecturer,
                                 on_delete=models.CASCADE)
    team_assigned = models.OneToOneField(Team, null=True)

    def __str__(self):
        return self.name
