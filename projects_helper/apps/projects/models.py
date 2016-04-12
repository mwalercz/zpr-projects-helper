from django.core.urlresolvers import reverse
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    lecturer = models.ForeignKey('lecturers.Lecturer',
                                 on_delete=models.CASCADE)
    team_assigned = models.OneToOneField('teams.Team', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:detail', args=[str(self.id)])
